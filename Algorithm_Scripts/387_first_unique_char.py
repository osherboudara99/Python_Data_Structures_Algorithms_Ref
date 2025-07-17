# https://leetcode.com/problems/first-unique-character-in-a-string/description/
# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

# Example 1:
# Input: s = "leetcode"
# Output: 0
# Explanation:
# The character 'l' at index 0 is the first character that does not occur at any other index.

# Example 2:
# Input: s = "loveleetcode"
# Output: 2

# Example 3:
# Input: s = "aabb"
# Output: -1

# Constraints:
# 1 <= s.length <= 105
# s consists of only lowercase English letters.

def first_unique_char(s:str) -> int:
    counts = {} 

    for i in s:
        counts[i] = counts.get(i, 0) + 1 
    
    for i in range(len(s)):
        if counts[s[i]] == 1:
            return i 
    return -1

print(first_unique_char('leetcode'))

print(first_unique_char('loveleetcode'))

print(first_unique_char('aabb'))


# Approach: Hash Map Frequency Count (Two Passes)
# 1. First pass: Count the frequency of each character in the string using a hash map.
# 2. Second pass: Iterate through the original string again to find the first character with a count of 1.
# 3. Return the index of the first unique character. If none found, return -1.

# Time Complexity: O(n)
# - One pass to count frequencies, one pass to find the first unique character.

# Space Complexity: O(1)
# - Since there are at most 26 lowercase English letters, the hash map uses constant space.

