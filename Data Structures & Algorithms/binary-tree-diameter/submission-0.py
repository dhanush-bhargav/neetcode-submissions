# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    max_diameter = 0

    def maxDepth(self, root:Optional[TreeNode]) -> int:
        if root is None:
            return 0

        depth_left = self.maxDepth(root.left)
        depth_right = self.maxDepth(root.right)

        self.max_diameter = max(self.max_diameter, (depth_left + depth_right))

        return 1 + max(depth_left, depth_right)


    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_depth = self.maxDepth(root)
        return self.max_diameter
        