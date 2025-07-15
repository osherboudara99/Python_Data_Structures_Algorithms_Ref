# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:
# Input: s = "rat", t = "car"
# Output: false

# Constraints:
# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.
# Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?


def is_anagram(s:str, t:str) -> bool:
    # O(n) time
    s_dict = {}
    t_dict = {}

    for i in s:
        s_dict[i] = s_dict.get(i, 0) +1 
    
    for j in t:
        t_dict[j] = t_dict.get(j, 0) + 1 

    return t_dict == s_dict


print(is_anagram(s = "anagram", t = "nagaram"))
print(is_anagram(s = "rat", t = "car"))


def is_anagram(s:str, t:str) -> bool:
    # O(n) time worst case, O(1) if both strings are different lengths
    if len(s) != len(t):
        return False 
    
    t_dict= {}
    s_dict= {} 

    for i in range(len(s)):
        s_dict[s[i]] = s_dict.get(s[i], 0) + 1 
        t_dict[t[i]] = t_dict.get(t[i], 0) + 1 

    return s_dict == t_dict

print(is_anagram(s = "anagram", t = "nagaram"))
print(is_anagram(s = "rat", t = "car"))

def is_anagram(s:str, t:str) -> bool:
    return sorted(s) == sorted(t)

print(is_anagram(s = "anagram", t = "nagaram"))
print(is_anagram(s = "rat", t = "car"))


# Approach 1: Frequency Count using Two Hash Maps (Two Passes)
# - Build separate frequency dictionaries for each string.
# - Compare the two dictionaries at the end.
# - Time: O(n), Space: O(1) if characters are limited (e.g., lowercase letters)

# Approach 2: Frequency Count using Two Hash Maps (Single Loop)
# - First check if lengths differ; if so, return False early.
# - Build both frequency dictionaries in one loop using index access.
# - Compare dictionaries.
# - Time: O(n), Space: O(1)

# Approach 3: Sorting
# - Sort both strings and compare the results.
# - Time: O(n log n) due to sorting, Space: O(n) depending on sorting implementation