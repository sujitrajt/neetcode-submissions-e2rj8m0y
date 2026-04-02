# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        result = []
        queue = deque([root])
        zigzag = True
        while queue:
            len_size = len(queue)
            current_level_nodes = deque()
            for i in range(len_size):
                node = queue.popleft()
                if zigzag:
                    current_level_nodes.append(node.val)
                else:
                    current_level_nodes.appendleft(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(current_level_nodes)
            zigzag = not zigzag
        return result
                    