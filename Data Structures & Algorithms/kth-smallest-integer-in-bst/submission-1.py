# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    flattened_tree = []

    def flatten_tree(self, root: Optional[TreeNode]):
        if not root:
            return
        else:
            self.flatten_tree(root.left)
            self.flattened_tree.append(root.val)
            self.flatten_tree(root.right)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.flattened_tree = []
        self.flatten_tree(root)
        print(self.flattened_tree)
        return self.flattened_tree[k-1]
        