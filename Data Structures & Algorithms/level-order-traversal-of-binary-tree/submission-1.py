# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        result = []
        q = deque()
        q.append(root)
        while q:
            q_length = len(q)
            level = []
            for i in range(q_length):
                curr = q.popleft()
                if curr:
                    q.append(curr.left)
                    q.append(curr.right)
                    level.append(curr.val)
            if level:
                result.append(level)
        return result
       