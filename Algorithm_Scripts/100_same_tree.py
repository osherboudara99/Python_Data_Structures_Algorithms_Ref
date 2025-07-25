# https://leetcode.com/problems/same-tree/description/

# Given the roots of two binary trees p and q, write a function to check if they are the same or not.
# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

# Example 1:
# Input: p = [1,2,3], q = [1,2,3]
# Output: true

# Example 2:
# Input: p = [1,2], q = [1,null,2]
# Output: false

# Example 3:
# Input: p = [1,2,1], q = [1,1,2]
# Output: false

# Constraints:
# The number of nodes in both trees is in the range [0, 100].
# -104 <= Node.val <= 104

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left 
        self.right = right 

def is_same_tree(p:Optional[TreeNode], q:Optional[TreeNode]) -> bool:
    if not p and not q:
        return True 
    if not p or not q:
        return False 
    if p.val != q.val:
        return False 

    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)


p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(3)

q = TreeNode(1)
q.left = TreeNode(2)
q.right = TreeNode(3)

print(is_same_tree(p, q))

p = TreeNode(1)
p.left = TreeNode(2)

q = TreeNode(1)
q.right = TreeNode(2)

print(is_same_tree(p, q))


p = TreeNode(1)
p.left = TreeNode(1)
p.right = TreeNode(2)

q = TreeNode(1)
q.left = TreeNode(2)
q.right = TreeNode(1)

print(is_same_tree(p, q))


# Approach: Recursive Tree Comparison (Depth-First Search)
# - Base Cases:
#   - If both nodes are None, return True (both trees are empty at this branch).
#   - If one node is None and the other is not, return False.
#   - If the values of the current nodes differ, return False.
# - Recursive Step:
#   - Recursively compare the left subtrees and the right subtrees.
#   - Return True only if both subtrees are identical.

# Time Complexity: O(n)
# - Each node is visited once, where n is the total number of nodes in both trees (assuming they have the same structure).

# Space Complexity: O(h)
# - h is the height of the tree (O(log n) for balanced, O(n) for unbalanced trees), due to the recursive call stack.

# Notes:
# - A simple and elegant recursive solution.
# - Can also be done iteratively with a queue or stack if needed.

