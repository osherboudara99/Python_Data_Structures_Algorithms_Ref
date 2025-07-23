# https://leetcode.com/problems/pascals-triangle/description/
# Given an integer numRows, return the first numRows of Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

# Example 1:
# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

# Example 2:
# Input: numRows = 1
# Output: [[1]]
 
# Constraints:
# 1 <= numRows <= 30

def generate_pascals_triangle(num_rows:int) -> list[list[int]]:
    result = [[1]]
    i = 0
    while len(result) < num_rows:
        prev = result[i]
        new_row = [1]

        for j in range(1, len(prev)):
            new_row.append(prev[j-1] + prev[j])

        new_row.append(1)
        result.append(new_row)
        i += 1 
    return result 


print(generate_pascals_triangle(1))
print(generate_pascals_triangle(2))
print(generate_pascals_triangle(4))
print(generate_pascals_triangle(5))
print(generate_pascals_triangle(6))

# Approach: Dynamic Row Construction
# - Start with the first row [1] in the result list.
# - For each new row:
#   - Begin and end with 1.
#   - Fill in the middle elements by summing adjacent elements from the previous row.
#   - Append the newly created row to the result list.
# - Repeat until `num_rows` is reached.

# Time Complexity: O(num_rows^2)
# - Each row has up to `num_rows` elements, and we build each row iteratively.

# Space Complexity: O(num_rows^2)
# - We store the entire triangle in memory as a list of lists.

# Notes:
# - Elegant use of dynamic programming (bottom-up).
# - Avoids recomputation by building off the previously computed row.
# - Simple and efficient for generating Pascal’s Triangle.

