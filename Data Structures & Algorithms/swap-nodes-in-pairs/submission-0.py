# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode(next=head)
        while cur.next and cur.next.next:
            first = cur.next
            second = cur.next.next
            temp = second.next
            second.next = first
            cur.next = second
            first.next = temp
            cur = first
        return dummy.next
