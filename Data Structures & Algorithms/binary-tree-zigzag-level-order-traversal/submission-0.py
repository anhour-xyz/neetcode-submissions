# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        res = []
        q = deque()
        q.append(root)
        level = 1
        while q:
            temp = []
            for i in range(len(q)):
                node = q.popleft()
                temp.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            if level % 2 == 0:
                res.append(temp[::-1])
            else:
                res.append(temp)
            level += 1
        return res