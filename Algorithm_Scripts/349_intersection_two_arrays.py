# https://leetcode.com/problems/intersection-of-two-arrays/description/
# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

# Example 1:
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]

# Example 2:
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# Explanation: [4,9] is also accepted.

# Constraints:
# 1 <= nums1.length, nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 1000

def intersection(nums1:list[int], nums2:list[int]) -> list[int]:
    results = [] 

    for i in nums1:
        if i in nums2 and i not in results:
            results.append(i)
    return results 

def intersection(nums1:list[int], nums2:list[int]) -> list[int]:
    return list(set(nums1) & set(nums2))


print(intersection([1,2,3], [3,3,3]))
print(intersection(nums1 = [1,2,2,1], nums2 = [2,2]))
print(intersection(nums1 = [4,9,5], nums2 = [9,4,9,8,4]))


# Approach 1: Brute Force with Membership Checks
# - Iterate over nums1
# - For each element, check:
#   1. If it's in nums2 (i in nums2) → O(n)
#   2. If it's not already in the result (i not in results) → O(m)
# - Append to results if both conditions are met

# Time Complexity: O(n * m), where m is size of nums2 or results
# Space Complexity: O(k), where k is the number of unique common elements

# Notes:
# - Inefficient for large arrays
# - Avoids duplicates manually


# Approach 2: Set Intersection
# - Convert both lists to sets to eliminate duplicates
# - Use set intersection (&) to find common elements
# - Convert the result back to a list

# Time Complexity: O(n + m)
# - Creating sets takes O(n + m)
# - Set intersection is efficient (typically linear)

# Space Complexity: O(n + m) for the sets

# Notes:
# - Very concise and Pythonic
# - Recommended for most use cases
