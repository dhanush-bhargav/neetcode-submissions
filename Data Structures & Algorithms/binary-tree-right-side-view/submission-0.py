# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        right_view = []
        q = deque()
        q.append(root)
        extracted = False
        while q:
            q_length = len(q)
            extracted = False
            for i in range(q_length):
                curr = q.popleft()
                if curr:
                    q.append(curr.right)
                    q.append(curr.left)
                    if not extracted:
                        right_view.append(curr.val)
                        extracted = True
        return right_view

