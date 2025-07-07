#  https://leetcode.com/problems/reverse-string/description/
# Write a function that reverses a string. The input string is given as an array of characters s.
# You must do this by modifying the input array in-place with O(1) extra memory.

# Example 1:

# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
# Example 2:

# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]

def reverse_string(s: list[str]):
    # O(n/2) -> O(n)
    left = 0 
    right = len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1 
        right -= 1
    return s 


def reverse_string(s: list[str]):
    # O(1)
    return s[::-1]


print(reverse_string(["h","e","l","l","o"]))
print(reverse_string(["H","a","n","n","a","h"]))


# Approach:
# Initialize two pointers: one at the start (left) and the other at the end (right).
# While left is less than right:
#   Swap the characters at left and right.
#   Increment left and decrement right.
# The array is reversed in place.

