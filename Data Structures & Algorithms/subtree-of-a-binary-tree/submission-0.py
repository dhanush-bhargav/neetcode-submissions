# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    is_subtree = False

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (p is None) and (q is None):
            return True

        if ((p is None) and (q is not None)) or ((p is not None) and (q is None)):
            return False

        if p.val != q.val:
            return False
        else:
            check_right = self.isSameTree(p.right, q.right)
            check_left = self.isSameTree(p.left, q.left)
            return (True & check_right & check_left)
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)
        return self.isSameTree(root, subRoot) or left or right
