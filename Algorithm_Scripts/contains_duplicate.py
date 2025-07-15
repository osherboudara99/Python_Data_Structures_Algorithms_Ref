# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: true
# Explanation:
# The element 1 occurs at the indices 0 and 3.

# Example 2:
# Input: nums = [1,2,3,4]
# Output: false
# Explanation:
# All elements are distinct.


# Example 3:
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

# Constraints:
# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109

def contains_duplicate(nums:list[int]) -> bool:

    d = {}
    for i in nums:
        d[i] = d.get(i, 0) + 1 

        if d.get(i) > 1:
            return True 
    return False 


print(contains_duplicate([1,2,3,1]))
print(contains_duplicate([1,2,3,4]))
print(contains_duplicate([1,1,1,3,3,4,3,2,4,2]))

def contains_duplicate(nums:list[int]) -> bool: 
    return len(nums) == len(set(nums))


print(contains_duplicate([1,2,3,1]))
print(contains_duplicate([1,2,3,4]))
print(contains_duplicate([1,1,1,3,3,4,3,2,4,2]))


# Approach 1: Hash Map (Dictionary) Frequency Count
# - Use a dictionary to count occurrences of each number.
# - If any number appears more than once during iteration, return True immediately.
# - Time: O(n), Space: O(n)

# Approach 2: Set Comparison
# - Convert the list to a set (which removes duplicates).
# - If the set length is less than the list length, duplicates exist.
# - Time: O(n), Space: O(n)
