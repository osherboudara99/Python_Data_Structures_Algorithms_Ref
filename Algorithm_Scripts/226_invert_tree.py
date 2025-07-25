# https://leetcode.com/problems/invert-binary-tree/description/
# Given the root of a binary tree, invert the tree, and return its root.

# Example 1:
# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]

# Example 2:
# Input: root = [2,1,3]
# Output: [2,3,1]

# Example 3:
# Input: root = []
# Output: [] 

# Constraints:
# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val 
        self.left = left 
        self.right = right 


def invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if root is None:
        return None 
    else:
        root.left, root.right = root.right, root.left 
        invert_tree(root.left)
        invert_tree(root.right)
    return root

def bfs(root):
    current_node = root 
    result = []
    queue = [] 

    queue.append(current_node)

    while len(queue) > 0:
        current_node = queue.pop(0)
        result.append(current_node.val)
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)
    return result

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

print('Before:', bfs(root))
root = invert_tree(root)
print('After:', bfs(root))


root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

print('Before:', bfs(root))
root = invert_tree(root)
print('After:', bfs(root))

# Approach: Recursive Tree Traversal (Depth-First Search)
# - Base Case: If the node is None, return None (empty subtree).
# - Recursive Case:
#   - Swap the left and right child of the current node.
#   - Recursively invert the left and right subtrees.
# - This modifies the tree in place and returns the root of the inverted tree.

# Time Complexity: O(n)
# - Each node is visited exactly once, where n is the number of nodes in the tree.

# Space Complexity: O(h)
# - h is the height of the tree (O(log n) for balanced tree, O(n) for skewed tree).
# - This is due to the recursive call stack.

# Notes:
# - A classic example of using recursion for tree manipulation.
# - Can also be solved iteratively using a queue or stack (BFS or DFS).

