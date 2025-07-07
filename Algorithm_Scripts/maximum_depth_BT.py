# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.



# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: 3
# Example 2:

# Input: root = [1,null,2]
# Output: 2
 

# Constraints:

# The number of nodes in the tree is in the range [0, 104].
# -100 <= Node.val <= 100


from typing import Optional


class TreeNode: 
    def __init__(self, val=0, left=None, right=None):
        self.val = val 
        self.left = left 
        self.right = right 


def max_depth(root: Optional[TreeNode]) -> int:
    # O(log(n))
    if root is None:
        return 0
    else:
        return 1+max(max_depth(root.left), max_depth(root.right))


root = TreeNode(val = 1)
root.left = TreeNode(val = 2)
root.right = TreeNode(val = 3)
root.right.left = TreeNode(val = 4)
root.left.right = TreeNode(val = 4)
print(max_depth(root))

root = TreeNode(val = 1)
root.left = TreeNode(val = 2)
root.left.right = TreeNode(val = 4)
root.left.right.left = TreeNode(val = 4)
print(max_depth(root))

# Approach
# If root is None then return 0 
# Else return recursively 1 + the maximum level between the left of root and right of root 
# Note: This will traverse the tree where it can and it adds one for each level. To avoid adding 1 twice for each left and right, we use max so we add it in once