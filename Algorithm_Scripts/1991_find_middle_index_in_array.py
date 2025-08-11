# https://leetcode.com/problems/find-the-middle-index-in-array/description/?envType=problem-list-v2&envId=prefix-sum
# Given a 0-indexed integer array nums, find the leftmost middleIndex (i.e., the smallest amongst all the possible ones).
# A middleIndex is an index where nums[0] + nums[1] + ... + nums[middleIndex-1] == nums[middleIndex+1] + nums[middleIndex+2] + ... + nums[nums.length-1].
# If middleIndex == 0, the left side sum is considered to be 0. Similarly, if middleIndex == nums.length - 1, the right side sum is considered to be 0.
# Return the leftmost middleIndex that satisfies the condition, or -1 if there is no such index.

# Example 1:
# Input: nums = [2,3,-1,8,4]
# Output: 3
# Explanation: The sum of the numbers before index 3 is: 2 + 3 + -1 = 4
# The sum of the numbers after index 3 is: 4 = 4

# Example 2:
# Input: nums = [1,-1,4]
# Output: 2
# Explanation: The sum of the numbers before index 2 is: 1 + -1 = 0
# The sum of the numbers after index 2 is: 0

# Example 3:
# Input: nums = [2,5]
# Output: -1
# Explanation: There is no valid middleIndex.

# Constraints:
# 1 <= nums.length <= 100
# -1000 <= nums[i] <= 1000


def find_middle_index(nums:list[int]) ->int:
    left_sum = [nums[0]] * len(nums)
    right_sum = [nums[-1]] * len(nums)

    for left in range(1, len(nums)):
        left_sum[left] = left_sum[left-1] + nums[left]

    for right in range(len(nums)-2, -1, -1):
        right_sum[right] = right_sum[right+1] + nums[right]

    for i in range(len(nums)):
        if left_sum[i] == right_sum[i]:
            return i 
    return -1 

def find_middle_index(nums:list[int]) -> int:
    left_sum = 0 
    total_sum = sum(nums)

    for i in range(len(nums)):
        right_sum = total_sum - left_sum - nums[i] 

        if left_sum == right_sum:
            return i 
        left_sum += nums[i]
    return -1

print(find_middle_index(nums = [2,3,-1,8,4]))
print(find_middle_index(nums = [1,-1,4]))
print(find_middle_index(nums = [2,5]))


# Approach: Prefix Sum from Both Ends
# - Create two arrays of length n:
#     1. left_sum[i] = sum of nums[0] through nums[i] (inclusive).
#     2. right_sum[i] = sum of nums[i] through nums[n-1] (inclusive).
# - Initialize both arrays with repeated first/last values for convenience.
# - Fill left_sum from left to right:
#     - Each position accumulates the previous prefix sum plus the current element.
# - Fill right_sum from right to left:
#     - Each position accumulates the next suffix sum plus the current element.
# - Iterate through all indices:
#     - If left_sum[i] == right_sum[i], return i (the middle index).
# - If no such index exists, return -1.
#
# Time Complexity: O(n)
# - Three passes through the array of length n.
#
# Space Complexity: O(n)
# - Stores two extra arrays of length n.
#
# Notes:
# - This is a clear and direct method to find the middle index.
# - Not space-optimal; can be reduced to O(1) space by using a running sum and total sum.


# Approach: Single Pass with Running Sums
# - First, compute total_sum = sum(nums) to know the overall sum of the array.
# - Initialize left_sum = 0 to track the sum of elements to the left of index i.
# - Loop through each index i:
#     1. Calculate right_sum = total_sum - left_sum - nums[i].
#     2. If left_sum == right_sum, return i (this is the middle index).
#     3. Update left_sum += nums[i] before moving to the next iteration.
# - If no middle index is found, return -1.
#
# Time Complexity: O(n)
# - Single pass through nums after computing total_sum.
#
# Space Complexity: O(1)
# - Uses only constant extra space for variables.
#
# Notes:
# - Works for arrays containing negative numbers.
# - Order of updates is important: check before adding nums[i] to left_sum.
# - Equivalent to checking if the prefix sum before index i equals the suffix sum after index i.

