# https://leetcode.com/problems/product-of-array-except-self/description/
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

# Example 1:
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

# Example 2:
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]

# Constraints:
# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.

# Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)


def product_except_self(nums:list[int]) -> list[int]:
    result = [1] * len(nums)
    prefix_sum = 1 
    suffix_sum = 1 

    for left in range(1, len(nums)):
        prefix_sum *= nums[left-1]
        result[left] = prefix_sum 
    
    for right in range(len(nums)-2, -1, -1):
        suffix_sum *= nums[right+1]
        result[right] *= suffix_sum 
    
    return result 

print(product_except_self(nums = [1,2,3,4]))
print(product_except_self(nums = [-1,1,0,-3,3]))


# Approach:
# Prefix & Suffix Products Approach — 
# 1. First pass (prefix): Compute the running product of all elements 
#     before the current index and store it in the result array.
# 2. Second pass (suffix): Traverse from right to left, multiplying each 
#     position in result by the running product of elements after that index.
# 3. This avoids division and achieves O(n) time complexity.

# Time Complexity:
# O(n) — Each element is visited twice (once for prefix, once for suffix).

# Space Complexity:
# O(1) extra space — Output array is not counted towards extra space.