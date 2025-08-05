# https://leetcode.com/problems/two-sum/description/
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.


# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]
 
# Constraints:
# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.

def two_sum(nums:list[int], target:int) -> list[int]:
    for i in range(len(nums) - 1):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]
    return [] 

print(two_sum(nums = [2,7,11,15], target = 9))
print(two_sum(nums = [3,2,4], target = 6))
print(two_sum(nums = [3,3], target = 6))


def two_sum(nums:list[int], target:int) -> list[int]:
    traversed_nums = {} 
    for i in range(len(nums)):
        compliment = target - nums[i]
        if compliment in traversed_nums:
            return [traversed_nums[compliment], i]
        traversed_nums[nums[i]] = i
    return []

print(two_sum(nums = [2,7,11,15], target = 9))
print(two_sum(nums = [3,2,4], target = 6))
print(two_sum(nums = [3,3], target = 6))



# Approach 1: Brute Force (Nested Loops)
# - Compare every pair of numbers in the list.
# - If their sum equals the target, return their indices.
#
# Time Complexity: O(n^2)
# - Two nested loops: for each element, check every other element.
#
# Space Complexity: O(1)
# - No extra space is used aside from variables.
#
# Notes:
# - Simple to implement but inefficient for large input sizes.
# - Only useful for small datasets or as a starting point.

# Approach 2: Hash Map (Optimal Solution)
# - Traverse the list once while maintaining a dictionary of visited numbers and their indices.
# - For each number, calculate the complement needed to reach the target.
# - If the complement is already in the dictionary, return the pair of indices.
# - Otherwise, store the current number in the dictionary.
#
# Time Complexity: O(n)
# - Single pass through the array with O(1) average-time hash map lookups.
#
# Space Complexity: O(n)
# - Hash map stores up to n elements in the worst case.
#
# Notes:
# - Highly efficient and the most common approach in interviews.
# - Avoids unnecessary nested iterations by leveraging hashing.
