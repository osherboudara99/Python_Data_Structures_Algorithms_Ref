# https://leetcode.com/problems/valid-parentheses/description/?envType=problem-list-v2&envId=oizxjoit
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 
# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true

# Example 3:
# Input: s = "(]"
# Output: false

# Example 4:
# Input: s = "([])"
# Output: true

# Example 5:
# Input: s = "([)]"
# Output: false

# Constraints:
# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.


def is_valid(s:str) -> bool:
    stack = []  
    mapping = {'(':')' , '{':'}', '[':']'}
    if len(s) % 2 == 0:
        return False 
    
    for i in s:
        if i in mapping.keys():
            stack.append(i)
        else:
            if stack and i == mapping[stack[-1]]:
                stack.pop() 
            else:
                return False 
    if stack:
        return False 
    return True 

def is_valid(s:str) -> bool:
    stack = [] 
    mapping = {'(':')' , '{':'}', '[':']'}

    for i in s:
        if i in mapping.keys():
            stack.append(i)
        else:
            if not stack or i != mapping[stack[-1]]:
                return False 
            stack.pop() 
    return not stack 

def is_valid(s:str) -> bool:
    stack = [] 
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping.values():
            stack.append(char) 
        else:
            if not stack or mapping[char] != stack.pop():
                return False 
    return not stack

print(is_valid(s = "()"))
print(is_valid(s = "()[]{}"))
print(is_valid(s = "(]"))
print(is_valid(s = "([])"))
print(is_valid(s = "([)]"))
print(is_valid(s = ')}'))
print(is_valid(s = '}{}'))



# Approach 1: Stack with Opening-to-Closing Mapping
# - Goal: Check if a string of parentheses/brackets/braces is valid (all open brackets closed correctly in order).
# - Idea:
#     - Use a stack to track opening brackets.
#     - For each character:
#         - If it’s an opening bracket, push onto stack.
#         - If it’s a closing bracket, check if it matches the top of the stack.
#           - If it matches, pop from stack.
#           - Otherwise, the string is invalid.
# - Steps:
#     1. Initialize an empty stack and a dictionary mapping open->close.
#     2. Loop through each character in s:
#         - Push open brackets to stack.
#         - For closing brackets, validate against stack top.
#     3. After processing, return True if stack is empty; otherwise False.
#
# Notes on Implementation 1:
# - Includes an incorrect early check: `if len(s) % 2 == 0: return False` (this should be `!= 0` or removed). 
#   Length check alone is not sufficient for validity.

# Approach 2: Stack with Early Return
# - Same as Approach 1, but cleaner:
#     - For closing brackets, immediately return False if stack is empty or top does not match.
#     - Pop from stack only when valid.
# - Time Complexity: O(n)
# - Space Complexity: O(n)
# - Notes:
#     - Correctly handles empty string and unmatched brackets.
#     - Cleaner and more Pythonic than Approach 1.

# Approach 3: Stack with Closing-to-Opening Mapping
# - Idea: Map closing brackets to their corresponding opening brackets.
# - For each character:
#     - If it’s an opening bracket, push onto stack.
#     - If it’s a closing bracket:
#         - Stack must not be empty and top must match mapping[char], otherwise return False.
#         - Pop the matched opening bracket.
# - Time Complexity: O(n)
# - Space Complexity: O(n)
# - Notes:
#     - Often considered the cleanest approach.
#     - No need to differentiate opening and closing keys in mapping; logic handles both cleanly.

