# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur = head
        n = 0
        while cur:
            n += 1
            cur = cur.next
        p0 = dummy = ListNode(next=head)
        while n >= k:
            n -= k
            cur = p0.next
            pre = None
            for _ in range(k):
                temp = cur.next
                cur.next = pre
                pre = cur
                cur = temp
            tail = p0.next
            tail.next = cur
            p0.next = pre
            p0 = tail
        return dummy.next