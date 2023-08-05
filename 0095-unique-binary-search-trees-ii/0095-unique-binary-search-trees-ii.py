class Solution(object):
    def generateTrees(self, n):
        def generate_trees_helper(start, end):
            if start > end:
                return [None]
            result = []
            for root_val in range(start, end + 1):
                left_subtrees = generate_trees_helper(start, root_val - 1)
                right_subtrees = generate_trees_helper(root_val + 1, end)
                for left_subtree in left_subtrees:
                    for right_subtree in right_subtrees:
                        root = TreeNode(root_val)
                        root.left = left_subtree
                        root.right = right_subtree
                        result.append(root)
            return result
        return generate_trees_helper(1, n)