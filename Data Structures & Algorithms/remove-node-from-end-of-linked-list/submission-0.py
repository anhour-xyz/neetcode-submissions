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
        index = length - n
        if index == 0: return head.next
        cnt = 0
        temp = head
        while temp:
            if cnt == index-1 and temp.next.next:
                temp.next = temp.next.next
                break
            temp = temp.next
            cnt += 1

        return head
