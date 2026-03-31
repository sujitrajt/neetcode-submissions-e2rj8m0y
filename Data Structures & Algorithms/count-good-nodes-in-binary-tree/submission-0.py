# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root,max_):
            if root is None:
                return 0 
            count = 0 
            if root.val >= max_:
                count += 1
                max_ = root.val

            left = dfs(root.left, max_)
            right = dfs(root.right, max_)
            return count + left + right
        return dfs(root, -float("inf"))