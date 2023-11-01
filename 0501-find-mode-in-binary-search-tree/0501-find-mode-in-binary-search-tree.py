# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def dfs(node,counter):
            if not node:
                return
            counter[node.val]+=1
            dfs(node.left,counter)
            dfs(node.right,counter)
        counter = defaultdict(int)
        dfs(root,counter)
        max_freq = max(counter.values())
        ans = []
        for key in counter:
            if counter[key] == max_freq:
                ans.append(key)
        return ans