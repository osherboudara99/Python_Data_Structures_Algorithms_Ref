# https://leetcode.com/problems/longest-common-prefix/description/
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

# Constraints:
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters if it is non-empty.


def longest_common_prefix(strs:list[str]) -> str:
        first_string = strs[0]
        common_prefix = '' 
        j = 0
        
        while j < len(first_string):

            count_matches = 0
            for word in strs[1:]:
                if len(word) - 1 >= j:
                    if first_string[j] == word[j]:
                        count_matches += 1 
                else:
                    return common_prefix
            
            if count_matches == len(strs[1:]):
                common_prefix += first_string[j]
            else:
                return common_prefix
            
            j += 1
        return common_prefix

def longest_common_prefix(strs:list[str]) -> str:
    if not strs:
        return '' 
    
    first_string = strs[0]
    common_prefix = '' 

    for i in range(len(first_string)):
        char = first_string[i]
        for word in strs[1:]:
            if len(word) <= i  or word[i] != char:
                return common_prefix 
        common_prefix += char 
    return common_prefix


print(longest_common_prefix(strs = ["flower","flow","flight"]))
print(longest_common_prefix(strs = ["dog","racecar","car"]))
print(longest_common_prefix(strs = ['ab', 'a']))



# Approach 1: Character-by-Character Comparison with Counter
# - Start with the first string as a reference.
# - For each character index:
#   - Compare the character with the same index in all other strings.
#   - If all strings match → append to prefix.
#   - If any mismatch or length issue → return the prefix immediately.
# - Uses a counter to count matches for each index.

# Time Complexity: O(n * m)
# - n = number of strings
# - m = length of the shortest string
# - Each character in the shortest string is compared across all other strings.

# Space Complexity: O(1)
# - Only stores the prefix string.

# Notes:
# - Works reliably but is slightly verbose due to the explicit counter logic.


# Approach 2: Character-by-Character Comparison (Simplified)
# - Same logic as Approach 1 but without using a counter.
# - Iterate through each character of the first string:
#   - For each character, check every other string.
#   - If mismatch or string is too short → return prefix immediately.
#   - Otherwise, append the character to prefix.

# Time Complexity: O(n * m)
# - Same as above.

# Space Complexity: O(1)
# - Only stores the prefix string.

# Notes:
# - Cleaner and more Pythonic.
# - Early termination makes it efficient for common mismatches.
