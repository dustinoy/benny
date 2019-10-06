# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
     def insertionSortList(self, head):
        newHead = ListNode(0)
        newHead.next = head 
        while head and head.next:
            if head.val > head.next.val:
                nodeToInsert = head.next
                cur = newHead
                while cur.next and cur.next.val<nodeToInsert.val:
                    cur = cur.next
                head.next = nodeToInsert.next
                nodeToInsert.next = cur.next
                cur.next = nodeToInsert
            else:
                head = head.next
            
        return newHead.next
