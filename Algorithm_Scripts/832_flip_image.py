# https://leetcode.com/problems/flipping-an-image/description/?envType=problem-list-v2&envId=bit-manipulation
# Given an n x n binary matrix image, flip the image horizontally, then invert it, and return the resulting image.
# To flip an image horizontally means that each row of the image is reversed.
# For example, flipping [1,1,0] horizontally results in [0,1,1].
# To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0.
# For example, inverting [0,1,1] results in [1,0,0].
 

# Example 1:
# Input: image = [[1,1,0],[1,0,1],[0,0,0]]
# Output: [[1,0,0],[0,1,0],[1,1,1]]
# Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
# Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]

# Example 2:
# Input: image = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
# Output: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
# Explanation: First reverse each row: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]].
# Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
 
# Constraints:
# n == image.length
# n == image[i].length
# 1 <= n <= 20
# images[i][j] is either 0 or 1.

def flip_invert_image(image:list[list[int]]) -> list[list[int]]:
    for i in range(len(image)):
        image[i] = image[i][::-1]
        for j in range(len(image[i])):
            if image[i][j] == 1:
                image[i][j] = 0 
            else:
                image[i][j] = 1 
    return image 


print(flip_invert_image(image = [[1,1,0],[1,0,1],[0,0,0]]))
print(flip_invert_image(image = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]))


# Approach: Reverse and Invert
# - Goal: Given a binary matrix, flip each row horizontally and then invert each bit.
# - Idea:
#     - Flipping horizontally means reversing the order of elements in each row.
#     - Inverting means replacing 1 with 0 and 0 with 1.
# - Steps:
#     1. Iterate through each row of the matrix.
#     2. Reverse the row using slicing (`[::-1]`).
#     3. Iterate through the reversed row and invert each bit:
#         - If 1 → change to 0
#         - If 0 → change to 1
#     4. Return the modified matrix.
#
# Time Complexity: O(n * m)
# - `n` = number of rows, `m` = number of columns.
# - Each element is visited exactly twice (once for reversing, once for inverting).
#
# Space Complexity: O(1)
# - In-place modification; no additional data structures used.
#
# Notes:
# - Works for any binary matrix (values 0 or 1 only).
# - The reversing step can also be done with two-pointer swapping to avoid creating a slice.
