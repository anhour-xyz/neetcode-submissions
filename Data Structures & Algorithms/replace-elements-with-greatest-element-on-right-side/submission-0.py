class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        post = arr[-1]
        res = [-1] * len(arr)
        for i in range(len(arr)-2,-1,-1):
            res[i] = post
            post = max(post,arr[i])
        return res
