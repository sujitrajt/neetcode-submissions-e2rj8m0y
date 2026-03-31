# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root,min_,max_):
            if root is None:
                return True
            if root.val <= min_ or root.val >= max_:
                return False 
            return dfs(root.left, min_, root.val) and dfs(root.right, root.val, max_)

        return dfs(root, float('-inf'), float('inf'))