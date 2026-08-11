# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    good_nodes = []

    def dfsMaintainBranchMax(self, root, branch_max):
        if not root:
            return 0
        res = 0
        if root.val >= branch_max:
            res += 1
            branch_max = root.val
        res += self.dfsMaintainBranchMax(root.left, branch_max)
        res += self.dfsMaintainBranchMax(root.right, branch_max)
        return res

    def goodNodes(self, root: TreeNode) -> int:
        if root:
            return 1 + self.dfsMaintainBranchMax(root.left, root.val) + self.dfsMaintainBranchMax(root.right, root.val)