# 199. Binary Tree Right Side View
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def bfs(root, level):
            if not root:
                return
            
            if len(view) == level:
                view.append(root.val)
            bfs(root.right, level + 1)
            bfs(root.left , level + 1)

        view = []
        bfs(root, 0)
        return view
