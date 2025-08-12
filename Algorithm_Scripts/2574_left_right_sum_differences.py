# https://leetcode.com/problems/left-and-right-sum-differences/description/?envType=problem-list-v2&envId=prefix-sum
# You are given a 0-indexed integer array nums of size n.
# Define two arrays leftSum and rightSum where:
# leftSum[i] is the sum of elements to the left of the index i in the array nums. If there is no such element, leftSum[i] = 0.
# rightSum[i] is the sum of elements to the right of the index i in the array nums. If there is no such element, rightSum[i] = 0.
# Return an integer array answer of size n where answer[i] = |leftSum[i] - rightSum[i]|.

# Example 1:
# Input: nums = [10,4,8,3]
# Output: [15,1,11,22]
# Explanation: The array leftSum is [0,10,14,22] and the array rightSum is [15,11,3,0].
# The array answer is [|0 - 15|,|10 - 11|,|14 - 3|,|22 - 0|] = [15,1,11,22].

# Example 2:
# Input: nums = [1]
# Output: [0]
# Explanation: The array leftSum is [0] and the array rightSum is [0].
# The array answer is [|0 - 0|] = [0].
 
# Constraints:
# 1 <= nums.length <= 1000
# 1 <= nums[i] <= 105


def left_right_sum_differences(nums:list[int]) -> int:
    left_sum = [0] * len(nums)
    right_sum = [0]* len(nums)
    answer = [0] * len(nums)

    for i in range(1, len(nums)):
        left_sum[i] = left_sum[i-1] + nums[i-1]

    for i in range(len(nums)-2, -1, -1):
        right_sum[i] =right_sum[i+1] + nums[i+1]
    
    for i in range(len(nums)):
        answer[i] = abs(left_sum[i] - right_sum[i])

    return answer 


def left_right_sum_differences(nums:list[int]) -> int:
    left = 0 
    right = sum(nums) 
    answer = []

    for i in range(len(nums)):
        left += nums[i] 
        answer.append(abs(left - right))
        right -= nums[i]
    return answer

def left_right_sum_differences(nums:list[int]) -> int:
    left = 0 
    total = sum(nums)
    answer= []
    for i in range(len(nums)):
        right = total - left - nums[i]
        answer.append(abs(left-right))
        left += nums[i]
    return answer


print(left_right_sum_differences(nums = [10,4,8,3]))
print(left_right_sum_differences(nums = [1]))
print(left_right_sum_differences(nums = [1,2,3,4]))


# Approach 1: Prefix and Suffix Sum Arrays
# - Goal: For each index i, compute |sum(nums[:i]) - sum(nums[i+1:])|
# - Use two helper arrays:
#     left_sum[i]  = sum of all elements before index i.
#     right_sum[i] = sum of all elements after index i.
# - Steps:
#     1. Initialize left_sum and right_sum to all zeros.
#     2. Fill left_sum by accumulating from left to right (excluding nums[i]).
#     3. Fill right_sum by accumulating from right to left (excluding nums[i]).
#     4. For each i, answer[i] = abs(left_sum[i] - right_sum[i]).
#
# Time Complexity: O(n)
# - Two passes to fill prefix/suffix arrays and one pass to compute differences.
#
# Space Complexity: O(n)
# - Extra arrays for left_sum, right_sum, and answer.
#
# Notes:
# - Works for any integers, positive or negative.
# - Index i itself is excluded from both left_sum[i] and right_sum[i].


# Approach 2: Running Totals with Two Pointers
# - Goal: For each index i, compute |sum(nums[:i+1]) - sum(nums[i:])| while iterating once.
# - Maintain two variables:
#     left  = sum of elements processed so far (including current).
#     right = sum of elements remaining (including current) at start of iteration.
# - Steps:
#     1. Initialize left = 0, right = sum(nums).
#     2. For each i:
#         a. Add nums[i] to left.
#         b. Append abs(left - right) to answer.
#         c. Subtract nums[i] from right.
#
# Time Complexity: O(n)
# - Single pass through nums.
#
# Space Complexity: O(1) extra (aside from the output array).
#
# Notes:
# - This version includes nums[i] in both left and right during the calculation
#   before adjusting right, which still yields correct results in this setup.
# - More memory-efficient than Approach 1.


# Approach 3: On-the-fly Right Sum Calculation
# - Goal: For each index i, compute |sum(nums[:i]) - sum(nums[i+1:])| without extra arrays.
# - Maintain:
#     left  = sum of elements before i.
#     total = sum(nums), used to compute right on the fly.
# - Steps:
#     1. Initialize left = 0, total = sum(nums).
#     2. For each i:
#         a. right = total - left - nums[i] (exclude nums[i] itself).
#         b. Append abs(left - right) to answer.
#         c. Add nums[i] to left.
#
# Time Complexity: O(n)
# - Single pass through nums.
#
# Space Complexity: O(1) extra (aside from the output array).
#
# Notes:
# - This is the most space-efficient form while still being clear.
# - Explicitly avoids including nums[i] in either left or right.

