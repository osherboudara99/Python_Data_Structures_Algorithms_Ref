# Given a 0-indexed string word and a character ch, reverse the segment of word that starts at index 0 and ends at the index of the first occurrence of ch (inclusive). If the character ch does not exist in word, do nothing.
# For example, if word = "abcdefd" and ch = "d", then you should reverse the segment that starts at 0 and ends at 3 (inclusive). The resulting string will be "dcbaefd".
# Return the resulting string.

# Example 1:
# Input: word = "abcdefd", ch = "d"
# Output: "dcbaefd"
# Explanation: The first occurrence of "d" is at index 3. 
# Reverse the part of word from 0 to 3 (inclusive), the resulting string is "dcbaefd".

# Example 2:
# Input: word = "xyxzxe", ch = "z"
# Output: "zxyxxe"
# Explanation: The first and only occurrence of "z" is at index 3.
# Reverse the part of word from 0 to 3 (inclusive), the resulting string is "zxyxxe".

# Example 3:
# Input: word = "abcd", ch = "z"
# Output: "abcd"
# Explanation: "z" does not exist in word.
# You should not do any reverse operation, the resulting string is "abcd".
 
# Constraints:
# 1 <= word.length <= 250
# word consists of lowercase English letters.
# ch is a lowercase English letter.

def reverse_prefix(word:str, ch:str) -> str:
    for i in range(len(word)):
        if word[i] == ch:
            return word[i::-1] + word[i+1:]
    return word 

print(reverse_prefix(word = "abcdefd", ch = "d"))
print(reverse_prefix(word = "xyxzxe", ch = "z"))
print(reverse_prefix(word = "abcd", ch = "z"))

# Approach: Prefix Reversal
# - Iterate through the string to find the first occurrence of the character `ch`.
# - Once found:
#     1. Reverse the substring from index 0 to i (inclusive).
#     2. Concatenate the reversed prefix with the remaining part of the string (i+1 onward).
# - If `ch` is not found, return the original string unchanged.
#
# Time Complexity: O(n)
# - Looping to find `ch` is O(n), and slicing/reversal is also O(n).
#
# Space Complexity: O(n)
# - String slicing and concatenation create new strings.
#
# Notes:
# - Efficient for small and medium-sized strings.
# - If `ch` does not exist in `word`, no extra processing is done beyond the initial loop.
