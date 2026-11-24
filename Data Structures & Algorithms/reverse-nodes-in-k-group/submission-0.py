# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next
        last_tail = dummy = ListNode(next=head)
        while n >= k:
            n -= k
            pre = None
            cur = last_tail.next
            for _ in range(k):
                temp = cur.next
                cur.next = pre
                pre = cur
                cur = temp
            tail = last_tail.next
            tail.next = cur
            last_tail.next = pre
            last_tail = tail
        return dummy.next