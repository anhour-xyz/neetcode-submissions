# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        slow = dummy = ListNode()
        fast = head
        while fast:
            if fast.val != val:
                slow.next = fast
                slow = slow.next
            fast = fast.next
        return dummy.next