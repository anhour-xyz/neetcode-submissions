# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(root,preMax):
            if not root: return 0
            res = 1 if root.val >= preMax else 0
            preMax = max(preMax, root.val)
            res += dfs(root.left,preMax)
            res += dfs(root.right,preMax)
            return res
        
        return dfs(root,root.val)
