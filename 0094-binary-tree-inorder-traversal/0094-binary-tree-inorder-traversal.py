# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []
        stack = []
        current = root
        while current or stack:
            # Reach the leftmost node of the current node
            while current:
                stack.append(current)
                current = current.left
            # Current must be None at this point
            current = stack.pop()
            result.append(current.val)
            # We have visited the node and its left subtree.
            # Now, it's right subtree's turn
            current = current.right
        return result