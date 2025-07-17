#  https://leetcode.com/problems/word-pattern/
# Given a pattern and a string s, find if s follows the same pattern.
# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:
# Each letter in pattern maps to exactly one unique word in s.
# Each unique word in s maps to exactly one letter in pattern.
# No two letters map to the same word, and no two words map to the same letter.
 
# Example 1:
# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true
# Explanation:
# The bijection can be established as:

# 'a' maps to "dog".
# 'b' maps to "cat".

# Example 2:
# Input: pattern = "abba", s = "dog cat cat fish"
# Output: false

# Example 3:
# Input: pattern = "aaaa", s = "dog cat cat dog"
# Output: false

# Constraints:
# 1 <= pattern.length <= 300
# pattern contains only lower-case English letters.
# 1 <= s.length <= 3000
# s contains only lowercase English letters and spaces ' '.
# s does not contain any leading or trailing spaces.
# All the words in s are separated by a single space.


def words_pattern( pattern:str, s:str)->bool:
    d = {}
    s = s.split(' ')

    if len(pattern) != len(s):
        return False
    
    for i in range(len(pattern)):
        if pattern[i] not in d.keys():
            if s[i] in d.values():
                return False
            d[pattern[i]] = s[i]
        if s[i] != d[pattern[i]]:
            return False
    return True 


print(words_pattern(pattern = "abba", s = "dog cat cat dog"))
print(words_pattern(pattern = "abba", s = "dog cat cat fish"))
print(words_pattern(pattern = "aaaa", s = "dog cat cat dog"))


# Approach: Hash Map for Pattern Matching
# 1. Initialize a dictionary to store pattern-to-word mappings and split the sentence into words.
# 2. If the number of pattern characters doesn't match the number of words, return False.
# 3. Iterate through the pattern and corresponding words:
#    a. If the current pattern character is not in the dictionary:
#       - Check if the word is already mapped to another character (i.e., appears in the dictionary values). If so, return False.
#       - Otherwise, add the mapping from the pattern character to the word.
#    b. If the pattern character is already mapped, check if it maps to the current word.
#       - If not, return False.
# 4. If all mappings are consistent, return True.