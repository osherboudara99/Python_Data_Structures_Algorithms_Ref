# https://leetcode.com/problems/symmetric-tree/description/
# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

# Example 1:
# Input: root = [1,2,2,3,4,4,3]
# Output: true

# Example 2:
# Input: root = [1,2,2,null,3,null,3]
# Output: false
 

# Constraints:
# The number of nodes in the tree is in the range [1, 1000].
# -100 <= Node.val <= 100

# Follow up: Could you solve it both recursively and iteratively?

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val 
        self.left = left
        self.right = right 


def is_symmetric(root:Optional[TreeNode]):
    # Recursive
    def check(left, right):
        if not left and not right:
            return True 
        if not left or not right:
            return False 
        if left.val != right.val:
            return False 

        return check(left.left, right.right) and check(left.right, right.left)
    return check(root.left, root.right)

def is_symmetric(root:Optional[TreeNode]):
    # iterative
    if not root:
        return True 
    
    queue = [] 
    queue.append(root.left)
    queue.append(root.right)

    while queue:
        left = queue.pop(0)
        right = queue.pop(0)
        if not left and not right:
            continue 
        if not left or not right:
            return False
        if left.val != right.val:
            return False 

        queue.append(left.left)
        queue.append(right.right)
        queue.append(left.right)
        queue.append(right.left)
    return True
    

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)

print(is_symmetric(root))



root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.right = TreeNode(3)
root.right.right = TreeNode(3)

print(is_symmetric(root))


# Approach: Recursive Mirror Check (Depth-First Search)
# - The tree is symmetric if the left subtree is a mirror reflection of the right subtree.
# - Define a helper function `check(left, right)` that:
#   - Returns True if both left and right are None.
#   - Returns False if only one is None or values are not equal.
#   - Recursively checks if:
#     - left.left mirrors right.right AND
#     - left.right mirrors right.left

# Time Complexity: O(n)
# - Every node is visited once, where n is the number of nodes.

# Space Complexity: O(h)
# - h is the height of the tree (recursive call stack). O(log n) for balanced trees, O(n) for skewed trees.

# Notes:
# - Elegant and concise solution using DFS.
# - An iterative approach using a queue or stack is also possible for BFS-style symmetry check.

### --------------

# Approach: Iterative Mirror Check (Breadth-First Search)
# - Use a queue to compare nodes in pairs (left vs right).
# - Enqueue the left and right children in mirror order:
#   - left.left with right.right
#   - left.right with right.left
# - At each step:
#   - If both nodes are None, continue.
#   - If only one is None or values differ, return False.

# Time Complexity: O(n)
# - Every node is enqueued and dequeued once, where n is the number of nodes.

# Space Complexity: O(n)
# - In the worst case, the queue can grow up to the number of nodes at the widest level.

# Notes:
# - This is a non-recursive, BFS-style alternative to the recursive solution.
# - Useful when recursion depth may be an issue.



    
