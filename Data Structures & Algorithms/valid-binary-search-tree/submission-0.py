# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def dfs(self, root: Optional[TreeNode]):
        if not root:
            return -float('inf'), float('inf'), True 
        left_max, left_min, is_left_valid = self.dfs(root.left)
        right_max, right_min, is_right_valid = self.dfs(root.right)

        is_valid = is_left_valid & is_right_valid

        if (root.val>left_max and root.val<right_min):
            is_valid = is_valid & True
        else:
            is_valid = is_valid & False

        return max(max(root.val, right_max), left_max), min(min(root.val, right_min), left_min), is_valid


    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        _, _, result = self.dfs(root)
        return result