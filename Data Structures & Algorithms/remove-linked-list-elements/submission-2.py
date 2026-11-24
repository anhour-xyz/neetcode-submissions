# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        slow = dummy = ListNode(next=head)
        fast = head
        while fast:
            if fast.val != val:
                fast = fast.next
                slow = slow.next
            else:
                slow.next = fast.next
                fast = slow.next
        return dummy.next