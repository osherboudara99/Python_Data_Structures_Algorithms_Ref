# https://leetcode.com/problems/maximum-score-after-splitting-a-string/description/?envType=problem-list-v2&envId=prefix-sum
# Given a string s of zeros and ones, return the maximum score after splitting the string into two non-empty substrings (i.e. left substring and right substring).
# The score after splitting a string is the number of zeros in the left substring plus the number of ones in the right substring.

# Example 1:
# Input: s = "011101"
# Output: 5 
# Explanation: 
# All possible ways of splitting s into two non-empty substrings are:
# left = "0" and right = "11101", score = 1 + 4 = 5 
# left = "01" and right = "1101", score = 1 + 3 = 4 
# left = "011" and right = "101", score = 1 + 2 = 3 
# left = "0111" and right = "01", score = 1 + 1 = 2 
# left = "01110" and right = "1", score = 2 + 1 = 3

# Example 2:
# Input: s = "00111"
# Output: 5
# Explanation: When left = "00" and right = "111", we get the maximum score = 2 + 3 = 5

# Example 3:
# Input: s = "1111"
# Output: 3
 
# Constraints:
# 2 <= s.length <= 500
# The string s consists of characters '0' and '1' only.

def max_score(s:str) -> int:
    total_ones = s.count('1')
    one_count = 0 
    zero_count = 0 
    max_score = 0 

    for i in range(len(s)):
        if s[i] == '0':
            zero_count += 1 
        else:
            one_count += 1 

        current_score = total_ones + zero_count - one_count 
        max_score = max(max_score, current_score)
    return max_score 

print(max_score(s = "011101"))
print(max_score(s = "00111"))
print(max_score(s = "1111"))


# Approach: One-Pass Counting with Precomputed Total Ones
# - Goal: Split the binary string `s` into two non-empty parts to maximize:
#     score = (# of '0's in left part) + (# of '1's in right part).
# - Idea:
#     - Precompute total_ones = total number of '1's in the entire string.
#     - Iterate through `s`, tracking:
#         zero_count = '0's seen so far (left part).
#         one_count  = '1's seen so far (left part).
#     - At index i, right part has (total_ones - one_count) ones.
#       So: current_score = zero_count + (total_ones - one_count)
#       Simplifies to: current_score = total_ones + zero_count - one_count.
# - Steps:
#     1. Count total_ones in the string.
#     2. Initialize zero_count = one_count = max_score = 0.
#     3. Loop over s:
#         - Update zero_count or one_count based on s[i].
#         - Compute current_score.
#         - Update max_score if needed.
#     4. Return max_score.
#
# Time Complexity: O(n)
# - One pass to count ones, one pass to compute max score.
#
# Space Complexity: O(1)
# - Only a few counters used.
#
# Notes:
# - Avoids recomputing counts for each split using running totals.
# - We could skip checking the last index since both parts must be non-empty.

