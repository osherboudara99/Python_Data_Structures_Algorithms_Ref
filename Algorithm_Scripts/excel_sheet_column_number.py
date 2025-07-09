# Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.

# For example:

# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28 
# ...
 
# Example 1:
# Input: columnTitle = "A"
# Output: 1

# Example 2:
# Input: columnTitle = "AB"
# Output: 28

# Example 3:
# Input: columnTitle = "ZY"
# Output: 701
 
# Constraints:
# 1 <= columnTitle.length <= 7
# columnTitle consists only of uppercase English letters.
# columnTitle is in the range ["A", "FXSHRXW"].


def column_title_to_number(column_title:str)-> int:
    result = 0
    for char in column_title:
         # subtraction of ord('A') and adding 1 normalize code since ord('A') is 65 and we want A to equal 1 and so on
         # Multiply by 26 since base 26
        result = result * 26 + (ord(char) - ord('A') + 1)
    return result 


print(column_title_to_number('A'))
print(column_title_to_number('BC'))
print(column_title_to_number('ZS'))
print(column_title_to_number('ZSS'))

# Approach
# Initialize result as 0.
# For each character in the title:
#   Convert it to its position using 'ord(char) - ord('A') + 1'. You can also use 'ord(char) - 64'.
#   Multiply current result by 26 and add the position.
#   This is similar to converting a base-26 string to decimal.
# Return result