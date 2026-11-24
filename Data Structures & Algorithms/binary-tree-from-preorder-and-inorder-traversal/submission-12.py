# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index = {x:i for i,x in enumerate(inorder)}
        def dfs(pre_l, pre_r,in_l):
            if pre_l == pre_r: return None
            left_size = index[preorder[pre_l]] - in_l
            left = dfs(pre_l+1,pre_l+1+left_size,in_l)
            right = dfs(pre_l+1+left_size, pre_r, in_l+1+left_size)
            return TreeNode(preorder[pre_l],left,right)
        return dfs(0,len(preorder),0)