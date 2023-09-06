# 450. Delete Node in a BST
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def minvalNode(root):
            cur = root
            while cur and cur.left:
                # xét thêm cur trong trường hợp ngay từ đầu cây rỗng, 
                # khi đó sẽ lỗi khi truy xuất cur.left
                cur = cur.left
            return cur
        
        if not root:
            return None

        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.right:
                return root.left
            elif not root.left:
                return root.right
            else:
                minNode = minvalNode(root.right)
                root.val = minNode.val
                root.right = self.deleteNode(root.right, minNode.val)
                
        return root
