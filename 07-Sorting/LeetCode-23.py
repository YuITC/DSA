# 23. Merge k Sorted Lists
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        def merge2(list1, list2):
            tail = ListNode()
            dummy = tail
            while list1 and list2:
                if list1.val <= list2.val:
                    tail.next = list1
                    list1 = list1.next
                else:
                    tail.next = list2
                    list2 = list2.next
                tail = tail.next
            
            if list1: tail.next = list1
            if list2: tail.next = list2

            return dummy.next
        
        if not lists or len(lists) == 0:
            return None
        
        while len(lists) > 1:
            fused = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                fused.append(merge2(l1, l2))
            lists = fused

        return lists[0]
