# 707. Design Linked List
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:

    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        ptr = self.head.next
        while index > 0 and ptr:
            ptr = ptr.next
            index -= 1
        
        if index == 0 and ptr and ptr != self.tail:
            return ptr.val
        return -1

    def addAtHead(self, val: int) -> None:
        node = Node(val)
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node 

    def addAtTail(self, val: int) -> None:
        node = Node(val)
        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev.next = node
        self.tail.prev = node     

    def addAtIndex(self, index: int, val: int) -> None:
        ptr = self.head.next
        while ptr and index > 0:
            ptr = ptr.next
            index -= 1
        
        node = Node(val)
        if index == 0 and ptr:
            node.next = ptr
            node.prev = ptr.prev
            ptr.prev.next = node
            ptr.prev = node

    def deleteAtIndex(self, index: int) -> None:
        ptr = self.head.next
        while ptr and index > 0:
            ptr = ptr.next
            index -= 1
        
        if index == 0 and ptr and ptr != self.tail:
            ptr.prev.next = ptr.next
            ptr.next.prev = ptr.prev
