# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    lca = None

    def findNode(self, root: TreeNode, p: TreeNode, q: TreeNode) -> bool:
        if root is None:
            return False
        find_left = self.findNode(root.left, p, q)
        find_right = self.findNode(root.right, p, q)
        if find_left and find_right:
            self.lca = root
        if (root.val == p.val) or (root.val == q.val):
            if find_left or find_right:
                self.lca = root
            return (True | find_left | find_right)
        else:
            return (False | find_left | find_right)

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.findNode(root, p , q)
        return self.lca
        