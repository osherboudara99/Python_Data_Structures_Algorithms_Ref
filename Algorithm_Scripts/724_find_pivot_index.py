# https://leetcode.com/problems/find-pivot-index/description/?envType=problem-list-v2&envId=prefix-sum
# Given an array of integers nums, calculate the pivot index of this array.
# The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.
# If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.
# Return the leftmost pivot index. If no such index exists, return -1.

# Example 1:
# Input: nums = [1,7,3,6,5,6]
# Output: 3
# Explanation:
# The pivot index is 3.
# Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
# Right sum = nums[4] + nums[5] = 5 + 6 = 11

# Example 2:
# Input: nums = [1,2,3]
# Output: -1
# Explanation:
# There is no index that satisfies the conditions in the problem statement.

# Example 3:
# Input: nums = [2,1,-1]
# Output: 0
# Explanation:
# The pivot index is 0.
# Left sum = 0 (no elements to the left of index 0)
# Right sum = nums[1] + nums[2] = 1 + -1 = 0
 
# Constraints:
# 1 <= nums.length <= 104
# -1000 <= nums[i] <= 1000
 
# Note: This question is the same as 1991: https://leetcode.com/problems/find-the-middle-index-in-array/


def find_pivot_index(nums:list[int]) -> int:
    left_sum = [nums[0]] * len(nums)
    right_sum = [nums[-1]] * len(nums)

    for i in range(1, len(nums)):
        left_sum[i] = left_sum[i-1] + nums[i]
    
    for i in range(len(nums)-2, -1, -1):
        right_sum[i] = right_sum[i+1] +nums[i] 

    for i in range(len(nums)):
        if left_sum[i] == right_sum[i]:
            return i 
    return -1


def find_pivot_index(nums:list[int]) -> int:
    left = 0 
    total = sum(nums)
    
    for i in range(len(nums)):
        right = total - left - nums[i]

        if right == left:
            return i 
        left += nums[i]
    return -1

print(find_pivot_index(nums = [1,7,3,6,5,6]))
print(find_pivot_index(nums = [1,2,3]))
print(find_pivot_index(nums = [2,1,-1]))

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
#     - If left_sum[i] == right_sum[i], return i (the pivot index).
# - If no such index exists, return -1.
#
# Time Complexity: O(n)
# - Three passes through the array of length n.
#
# Space Complexity: O(n)
# - Stores two extra arrays of length n.
#
# Notes:
# - This is a clear and direct method to find the pivot index.
# - Not space-optimal; can be reduced to O(1) space by using a running sum and total sum.


# Approach: Single Pass with Running Sums
# - First, compute total = sum(nums) to know the overall sum of the array.
# - Initialize left = 0 to track the sum of elements to the left of index i.
# - Loop through each index i:
#     1. Calculate right = total - left - nums[i].
#     2. If left == right, return i (this is the pivot index).
#     3. Update left += nums[i] before moving to the next iteration.
# - If no pivot index is found, return -1.
#
# Time Complexity: O(n)
# - Single pass through nums after computing total.
#
# Space Complexity: O(1)
# - Uses only constant extra space for variables.
#
# Notes:
# - Works for arrays containing negative numbers.
# - Order of updates is important: check before adding nums[i] to left.
# - Equivalent to checking if the prefix sum before index i equals the suffix sum after index i.


