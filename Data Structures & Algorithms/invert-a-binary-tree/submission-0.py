# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def swapLeftRight(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return
        
        left = self.swapLeftRight(root.left)
        right = self.swapLeftRight(root.right)
        return TreeNode(root.val, right, left)


    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.swapLeftRight(root)