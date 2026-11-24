# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = dummy = ListNode(next=head)
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None

        pre = None
        while second:
            temp = second.next
            second.next = pre
            pre = second
            second = temp

        first, second = head, pre
        while first:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next
        return True