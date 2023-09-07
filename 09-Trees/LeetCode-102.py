# 102. Binary Tree Level Order Traversal
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        Q = deque()
        if root:
            Q.append(root)
        level = []
        while len(Q) > 0:
            tmp = []
            for i in range(len(Q)):
                cur = Q.popleft()
                tmp.append(cur.val)
                if cur.left : Q.append(cur.left)
                if cur.right: Q.append(cur.right)
            level.append(tmp)
        return level
