# https://leetcode.com/problems/running-sum-of-1d-array/description/?envType=problem-list-v2&envId=prefix-sum
# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
# Return the running sum of nums.

# Example 1:
# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

# Example 2:
# Input: nums = [1,1,1,1,1]
# Output: [1,2,3,4,5]
# Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].

# Example 3:
# Input: nums = [3,1,2,10,1]
# Output: [3,4,6,16,17]
 
# Constraints:
# 1 <= nums.length <= 1000
# -10^6 <= nums[i] <= 10^6

def running_sum(nums:list[int]) -> list[int]:
    for i in range(1, len(nums)):
        nums[i] = nums[i-1] + nums[i]
    return nums 

print(running_sum(nums = [1,2,3,4]))
print(running_sum(nums = [1,1,1,1,1]))
print(running_sum(nums = [3,1,2,10,1]))

# Approach: Cumulative Sum In-Place
# - Iterate over the list starting from index 1 (second element).
# - For each index i:
#     1. Update nums[i] to be nums[i-1] + nums[i].
#     2. This ensures each position stores the sum of all previous elements and itself.
# - Return the modified nums list.
#
# Time Complexity: O(n)
# - Single pass through the list, where n is the number of elements.
#
# Space Complexity: O(1)
# - No extra data structures used; modifies the list in place.
#
# Notes:
# - Efficient for large lists since it avoids creating an additional array.
# - The input list will be mutated; copy it first if the original must be preserved.
