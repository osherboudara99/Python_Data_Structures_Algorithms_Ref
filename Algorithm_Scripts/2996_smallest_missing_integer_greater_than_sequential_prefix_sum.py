# https://leetcode.com/problems/smallest-missing-integer-greater-than-sequential-prefix-sum/description/
# You are given a 0-indexed array of integers nums.
# A prefix nums[0..i] is sequential if, for all 1 <= j <= i, nums[j] = nums[j - 1] + 1. In particular, the prefix consisting only of nums[0] is sequential.
# Return the smallest integer x missing from nums such that x is greater than or equal to the sum of the longest sequential prefix.

# Example 1:
# Input: nums = [1,2,3,2,5]
# Output: 6
# Explanation: The longest sequential prefix of nums is [1,2,3] with a sum of 6. 6 is not in the array, therefore 6 is the smallest missing integer greater than or equal to the sum of the longest sequential prefix.

# Example 2:
# Input: nums = [3,4,5,1,12,14,13]
# Output: 15
# Explanation: The longest sequential prefix of nums is [3,4,5] with a sum of 12. 12, 13, and 14 belong to the array while 15 does not. Therefore 15 is the smallest missing integer greater than or equal to the sum of the longest sequential prefix.
 
# Constraints:
# 1 <= nums.length <= 50
# 1 <= nums[i] <= 50


def missing_int(nums:list[int]) -> int:
    sequential_sum = nums[0]

    for i in range(1,len(nums)):
        if nums[i] == nums[i-1] + 1:
            sequential_sum += nums[i]
        else:
            break 
    
    s = set(nums) 

    while sequential_sum in s:
        sequential_sum += 1 
    return sequential_sum

print(missing_int(nums = [1,2,3,2,5]))
print(missing_int(nums = [3,4,5,1,12,14,13]))
print(missing_int(nums = [4,5,6,7,8,8,9,4,3,2,7])) ## Expect 30
print(missing_int(nums = [29,30,31,32,33,34,35,36,37])) ## 297 
print(missing_int(nums = [29])) ## 30
print(missing_int(nums = [14,9,6,9,7,9,10,4,9,9,4,4])) ## 15


# Approach: Sequential Check + Set Lookup
# - Start with the first number and build a running sum assuming the numbers are sequential.
# - Iterate through the list:
#   - If the current number is consecutive (previous + 1), add it to the running sum.
#   - If there's a gap, stop the loop.
# - Convert the list into a set for O(1) membership checks.
# - Incrementally check from the running sum upward until a missing integer is found.

# Time Complexity:
# - O(n) for the initial loop through nums.
# - O(k) for the while loop in the worst case (k is the distance to the missing number).
# - Overall: O(n + k), but typically O(n).

# Space Complexity: O(n)
# - The set stores all numbers for fast membership checking.

# Notes:
# - Works when numbers are sorted.
# - Breaks early if a gap is found, making it efficient for early missing integers.
# - For very large inputs or unsorted arrays, a sum or XOR approach may be more efficient.



