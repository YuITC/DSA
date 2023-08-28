class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = Node(-1)
        self.tail = self.head
    
    def insertEnd(self, val):
        self.tail.next = Node(val)
        self.tail = self.tail.next
        
    def deleteMid(self, idx):
        i = 0
        cur = self.head
        while i < idx and cur:
            i += 1
            cur = cur.next
            
        if cur: cur.next = cur.next.next
        
    def print(self):
        cur = self.head.next
        while cur:
            print(cur.val, "->", end = " ")
            cur = cur.next
        print("None")
            
SLL = LinkedList()
for i in range(1, 10): SLL.insertEnd(i)
    
SLL.print()
SLL.deleteMid(3)
SLL.deleteMid(7)
SLL.print()
