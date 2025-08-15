# https://leetcode.com/problems/search-insert-position/description/?envType=problem-list-v2&envId=binary-search
# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.

# Example 1:
# Input: nums = [1,3,5,6], target = 5
# Output: 2

# Example 2:
# Input: nums = [1,3,5,6], target = 2
# Output: 1

# Example 3:
# Input: nums = [1,3,5,6], target = 7
# Output: 4
 
# Constraints:
# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums contains distinct values sorted in ascending order.
# -104 <= target <= 104


def search_insert_element(nums:list[int], target:int) -> int:

    low = 0 
    high = len(nums) - 1 

    while low <= high:

        mid = (low + high) // 2

        if nums[mid] == target:
            return mid 
        elif nums[mid] > target:
            high = mid -1 
        else:
            low = mid + 1 
    return low 


print(search_insert_element(nums = [1,3,5,6], target = 5))
print(search_insert_element(nums = [1,3,5,6], target = 2))
print(search_insert_element(nums = [1,3,5,6], target = 7))

# Approach: Binary Search
# - Goal: Find the index of `target` in a sorted list, or the insertion position if not found.
# - Use two pointers: `low` (start) and `high` (end).
# Steps:
#   1. While `low` <= `high`, compute `mid` as the middle index.
#   2. If `nums[mid]` equals `target`, return `mid`.
#   3. If `nums[mid]` > `target`, search the left half (`high = mid - 1`).
#   4. If `nums[mid]` < `target`, search the right half (`low = mid + 1`).
#   5. If loop ends without finding `target`, return `low` (insertion index).
#
# Time Complexity: O(log n)
# - Search space halves each iteration.
#
# Space Complexity: O(1)
# - Only uses constant extra variables.
