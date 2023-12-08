# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""

        # If the node is a leaf, return its value as a string
        if not root.left and not root.right:
            return str(root.val)

        # If there is no right child, don't include the pair of empty parentheses for the right child
        if not root.right:
            return str(root.val) + "(" + self.tree2str(root.left) + ")"

        # In all other cases, include both children
        return str(root.val) + "(" + self.tree2str(root.left) + ")(" + self.tree2str(root.right) + ")"