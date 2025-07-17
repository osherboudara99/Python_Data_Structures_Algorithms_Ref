# https://leetcode.com/problems/majority-element/description/
# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

# Example 1:
# Input: nums = [3,2,3]
# Output: 3

# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
 
# Constraints:
# n == nums.length
# 1 <= n <= 5 * 104
# -109 <= nums[i] <= 109
 
# Follow-up: Could you solve the problem in linear time and in O(1) space?
def majority_element(nums:list[int]) -> int:
        # O(n) time and O(n) space
        d = {}
        for i in nums:
            d[i] = d.get(i,0) + 1 
        
        max_value = 0
        majority_element = None
        for key in d.keys():
            if max_value < d[key]:
                max_value = d[key]
                majority_element = key
        return majority_element


def majority_element(nums:list[int]) -> int:
    # O(n) time and O(n) space
    # Cleaner version
    d = {}
    max_count = 0
    majority_element = None
    for i in nums:
        d[i] = d.get(i,0) + 1 
        if d[i] > max_count:
            majority_element = i
            max_count = d[i]

    return majority_element


def majority_element(nums:list[int]) -> int:
    # O(n) time and O(1) space
    candidate = nums[0]
    count = 0

    for i in nums:
        if candidate == i:
            count += 1
        else:
            if count == 0:
                candidate = i 
                count = 1 
            else:
                count-= 1
    return candidate


print(majority_element([5,4,3,4,5,5,5,5,5,5,1,2,3]))

print(majority_element([5,4,4,5,5]))


# Intuition (Boyer-Moore Voting Algorithm):
# If an element is the majority, it will outbalance all other elements combined.
# Think of it like a voting system:
# The majority element gains a vote.
# Every different element cancels a vote.
# If the count drops to zero, we "elect" a new candidate.

# Approach:
# Start with the first number as the candidate.
# Traverse the list:
#   If the current number equals the candidate, increment the count.
#   Otherwise, decrement the count.
#   If count hits 0, pick the current number as the new candidate and reset count to 1.
# After one pass, the candidate is guaranteed to be the majority element (given that it exists by problem constraint).



