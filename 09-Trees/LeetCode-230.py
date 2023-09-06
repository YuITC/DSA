# 230. Kth Smallest Element in a BST
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.kth = 0
        self.ans = -1
        def LNR(root):
            if not root: return

            LNR(root.left)
            self.kth += 1
            if self.kth == k:
                self.ans = root.val
                return
            LNR(root.right)
        LNR(root)
        return self.ans
