# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
     def insertionSortList(self, head):
          # 把數列的第一項指定是頭
        newHead = ListNode(0)
        newHead.next = head 
        while head and head.next
            # 跳過已經排序好的   
            if head.val > head.next.val:
                nodeToInsert = head.next
               # 開始比較
                cur = newHead
                while cur.next and cur.next.val<nodeToInsert.val:
                    cur = cur.next
                    # 將基準值指定到下一個要找的值
                head.next = nodeToInsert.next
               # 插到比自己大的值之前
                nodeToInsert.next = cur.next
                cur.next = nodeToInsert
            else:
                head = head.next
            
        return newHead.next
