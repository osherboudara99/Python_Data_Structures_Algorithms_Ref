# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
# Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

# Example 1:
# Input: nums = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
# Explanation: [0,-10,5,null,-3,null,9] is also accepted:

# Example 2:
# Input: nums = [1,3]
# Output: [3,1]
# Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.
 

# Constraints:
# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums is sorted in a strictly increasing order.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val 
        self.left = left
        self.right = right 
    

def sorted_array_to_BST(nums:list[int]) -> Optional[TreeNode]:
    if not nums:
        return None 
    mid_index = len(nums) // 2 
    root = TreeNode(nums[mid_index])
    root.left = sorted_array_to_BST(nums[:mid_index])
    root.right = sorted_array_to_BST(nums[mid_index+1:])
    return root 

def bfs(root):
    current_node = root
    queue = [] 
    results = [] 
    queue.append(current_node)

    while len(queue) > 0:
        current_node = queue.pop(0)
        results.append(current_node.val)
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)
    return results

root = sorted_array_to_BST(nums = [-10,-3,0,5,9])

print(bfs(root))


root = sorted_array_to_BST(nums = [1,3])

print(bfs(root))


# Approach: Recursive Divide and Conquer
# - Choose the middle element of the current subarray as the root.
# - Recursively build the left subtree from the left half of the array.
# - Recursively build the right subtree from the right half of the array.
# - This ensures the tree is height-balanced because the array is split evenly at each level.

# Time Complexity: O(n)
# - Each element is visited once to be placed into the tree.

# Space Complexity: O(log n) average case (for recursion stack), O(n) worst case if input is skewed
    