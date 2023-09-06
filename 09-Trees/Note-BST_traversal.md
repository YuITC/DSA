<b> DFS traversal </b>
``` python
def inorder(root): # LNR traversal, O(n)
    if not root:
        return
    inorder(root.left)
    print(root.val)
    inorder(root.right)
    
def preorder(root): # NLR traversal, O(n)
    if not root:
        return
    print(root.val)
    preorder(root.left)
    preorder(root.right)
    
def postorder(root): # LRN traversal, O(n)
    if not root:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.val)
```
<b> BFS traversal </b>
``` python
def bfs(root): # O(n)
    Q = deque()
    if root: Q.append(root)
        
    level = 1
    while len(Q) > 0:
        print("level: ", level)
        for i in range(len(Q)):
            cur = Q.popleft()
            print(cur.val)
            if cur.left: Q.append(cur.left)
            if cur.right: Q.append(cur.right)
        level += 1
```
