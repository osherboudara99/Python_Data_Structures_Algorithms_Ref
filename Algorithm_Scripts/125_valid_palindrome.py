# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.

 
# Example 1:
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

# Example 2:
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.

# Example 3:
# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.

# Constraints:
# 1 <= s.length <= 2 * 105
# s consists only of printable ASCII characters.


def is_palindrome(s:str) -> str:
    s = ''.join(i.lower() for i in s if i.isalnum())
    left = 0
    right = len(s) - 1 

    while left < right:
        if s[left]!= s[right]:
            return False 
        left += 1 
        right -= 1 
    return True 

def is_palindrome(s:str) -> str:
    s = ''.join(i.lower() for i in s if i.isalnum())
    return s == s[::-1]


print(is_palindrome(s = "A man, a plan, a canal: Panama"))
print(is_palindrome(s = "race a car"))
print(is_palindrome(s = "race car"))
print(is_palindrome(s = " "))


# Approach 1: Two-Pointer Technique
# - Clean the string by removing non-alphanumeric characters and converting to lowercase.
# - Use two pointers (`left` and `right`) to compare characters from both ends moving toward the center.
# - If characters mismatch at any point, return False.
# - If all characters match, return True.

# Approach 2: Pythonic One-Liner
# - Clean the string as in the first approach.
# - Check if the cleaned string is equal to its reverse using slicing (`s[::-1]`).
# - Return True if they match, False otherwise.

# Time Complexity: O(n)
# Space Complexity: O(n)