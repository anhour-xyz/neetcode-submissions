# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        temp = []
        cur = head
        while cur:
            temp.append(cur.val)
            cur = cur.next
        
        i = 0
        j = len(temp) - 1
        res = []
        while i < j:
            res.append(temp[i])
            res.append(temp[j])
            i += 1
            j -= 1
        
        if len(temp) % 2 == 1: res.append(temp[len(temp)//2])
        
        cur = head
        i = 0
        while cur and i < len(res):
            cur.val = res[i]
            cur = cur.next
            i += 1