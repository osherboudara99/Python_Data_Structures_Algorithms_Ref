# https://leetcode.com/problems/single-number/description/
# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.

# Example 1:
# Input: nums = [2,2,1]
# Output: 1

# Example 2:
# Input: nums = [4,1,2,1,2]
# Output: 4

# Example 3:
# Input: nums = [1]
# Output: 1

# Constraints:

# 1 <= nums.length <= 3 * 104
# -3 * 104 <= nums[i] <= 3 * 104
# Each element in the array appears twice except for one element which appears only once.

def single_number(nums: list[int]) -> int:
    # O(n)
    x=0 
    for i in range(len(nums)):
        x ^= nums[i]
    return x 


print(single_number([1,2,3,1,2]))

print(single_number([1,1,1,1,1,1,2]))

print(single_number([7,8,7,8]))


# Approach:
# Initialize temp variable to zero
# Loop through number list
#   Bitwise XOR x and number at index (if x and i match, result is zero, else result is the addition of numbers in question)
# Return x