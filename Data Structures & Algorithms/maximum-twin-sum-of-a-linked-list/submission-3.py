# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        dummy = ListNode(0,head)
        slow = dummy
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        right = slow.next
        temp = self.reverse(right)
        cur = temp
        idx = head
        res = 0
        while cur:
            total = cur.val + idx.val
            cur = cur.next
            idx = idx.next
            res = max(res,total)
        return res


    def reverse(self,head):
        cur = head
        pre = None
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre