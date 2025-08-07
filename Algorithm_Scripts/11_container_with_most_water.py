# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.

# Example 1:
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
 
# Example 2:
# Input: height = [1,1]
# Output: 1
 
# Constraints:
# n == height.length
# 2 <= n <= 105
# 0 <= height[i] <= 104


def max_area(height:list[int]) -> int:
    max_area = 0 

    for i in range(len(height) - 1):
        for j in range(i+1, len(height)):
            current_area = min(height[i], height[j]) * (j-i) # Height * Width
            max_area = max(max_area, current_area) # if max_area < current_area: max_area = current_area
    return max_area

print(max_area(height = [1,8,6,2,5,4,8,3,7]))
print(max_area(height = [1,1]))


def max_area(height:list[int]) -> int:
    max_area = 0 
    left = 0 
    right = len(height) - 1 

    while left < right:
        current_area = min(height[left], height[right]) * (right - left)
        max_area = max(max_area, current_area)

        if height[left] < height[right]:
            left += 1 
        else:
            right -= 1 
    return max_area

print(max_area(height = [1,8,6,2,5,4,8,3,7]))
print(max_area(height = [1,1]))



# Approach 1: Brute Force
# - Use two nested loops to check every pair of lines.
# - For each pair, compute the area as `min(height[i], height[j]) * (j - i)`.
# - Track and return the maximum area encountered.
# - Time Complexity: O(n^2)
# - Space Complexity: O(1)

# Approach 2: Two-Pointer Technique (Optimized)
# - Use two pointers, one starting from the beginning and one from the end of the array.
# - Calculate the area between the two pointers.
# - Move the pointer with the shorter line inward, since moving the taller one cannot increase the area.
# - Repeat until the pointers meet.
# - Time Complexity: O(n)
# - Space Complexity: O(1)
