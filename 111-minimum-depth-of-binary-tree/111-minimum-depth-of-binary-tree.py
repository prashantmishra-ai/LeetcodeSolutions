# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def minDepth(self, root):
        if not root:
            return 0
        queue = deque()
        queue.append(root)
        minDepth = 0
        while queue:
            minDepth += 1
            levelSize = len(queue)
            for _ in range(levelSize):
                node = queue.popleft()
                if not node.left and not node.right:
                    return minDepth
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return minDepth