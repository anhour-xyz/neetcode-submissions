# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
        
        index = length - n + 1

        if index == 1:
            return head.next

        temp = dummy = head
        cnt = 1
        while temp:
            if cnt == index - 1:
                temp.next = temp.next.next
            cnt += 1
            temp = temp.next
        
        return dummy

