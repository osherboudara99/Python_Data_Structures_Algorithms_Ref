# https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/description/?envType=problem-list-v2&envId=prefix-sum
# Given an array of integers nums, you start with an initial positive value startValue.
# In each iteration, you calculate the step by step sum of startValue plus elements in nums (from left to right).
# Return the minimum positive value of startValue such that the step by step sum is never less than 1.

# Example 1:
# Input: nums = [-3,2,-3,4,2]
# Output: 5
# Explanation: If you choose startValue = 4, in the third iteration your step by step sum is less than 1.
# step by step sum
# startValue = 4 | startValue = 5 | nums
#   (4 -3 ) = 1  | (5 -3 ) = 2    |  -3
#   (1 +2 ) = 3  | (2 +2 ) = 4    |   2
#   (3 -3 ) = 0  | (4 -3 ) = 1    |  -3
#   (0 +4 ) = 4  | (1 +4 ) = 5    |   4
#   (4 +2 ) = 6  | (5 +2 ) = 7    |   2

# Example 2:
# Input: nums = [1,2]
# Output: 1
# Explanation: Minimum start value should be positive. 

# Example 3:
# Input: nums = [1,-2,-3]
# Output: 5
 
# Constraints:
# 1 <= nums.length <= 100
# -100 <= nums[i] <= 100



def min_start_value(nums:list[int]) -> int:
    for i in range(1, len(nums)):
        nums[i] = nums[i-1] + nums[i]
    
    minimum_prefix = min(nums)

    if minimum_prefix >= 1:
        return 1 
    
    compliment = 1 - minimum_prefix

    return compliment


def min_start_value(nums:list[int]) -> int:
    for i in range(1, len(nums)):
        nums[i] = nums[i-1] + nums[i] 
    
    minimum_prefix_sum = min(nums)

    return 1 if minimum_prefix_sum >= 1 else 1 - minimum_prefix_sum


def min_start_value(nums:list[int]) -> int:
    running_sum = 0 
    minimum_prefix_sum = float('inf')

    for num in nums:
        running_sum += num
        minimum_prefix_sum = min(running_sum, minimum_prefix_sum)
    
    return 1 if minimum_prefix_sum >= 1 else 1 - minimum_prefix_sum


print(min_start_value(nums = [-3,2,-3,4,2]))
print(min_start_value(nums = [1,2]))
print(min_start_value(nums = [1,-2,-3]))



# Approach: Running Sum with Minimum Prefix Tracking
# Goal:
#   Find the smallest positive integer start value such that when it is
#   added to the running sum of nums, the sum never drops below 1.
#
# Logic:
#   1. Compute the running prefix sums of nums.
#      - Either directly in the same list (mutating it) OR
#        track with a separate running_sum variable (non-mutating).
#   2. Track the smallest prefix sum encountered.
#   3. If this minimum prefix sum is already >= 1, return 1.
#   4. Otherwise, the smallest start value needed is (1 - minimum_prefix_sum).
#
# Variants:
#   - Version 1 & 2: Mutate nums to store cumulative sums, then find min.
#   - Version 3: Track running_sum in a separate variable to avoid mutation.
#
# Time Complexity: O(n)
#   - Single pass over nums.
#
# Space Complexity:
#   - Mutating version: O(1) extra space, modifies nums.
#   - Non-mutating version: O(1) extra space, keeps nums intact.
#
# Notes:
#   - Handles positive, negative, and zero values in nums.
#   - The non-mutating version is safer when nums is needed later.
