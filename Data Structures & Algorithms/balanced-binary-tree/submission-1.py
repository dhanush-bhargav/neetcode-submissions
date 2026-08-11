# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    is_balanced = True
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        depth_left = self.maxDepth(root.left)
        depth_right = self.maxDepth(root.right)

        if abs(depth_left - depth_right) <= 1:
            self.is_balanced = self.is_balanced & True
        else:
            self.is_balanced = self.is_balanced & False

        return 1 + max(depth_left, depth_right)


    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        depth = self.maxDepth(root)
        return self.is_balanced