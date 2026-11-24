class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = [-1] * len(arr)
        cur = arr[-1]
        for i in range(len(arr)-2,-1,-1):
            res[i] = cur
            cur = max(cur,arr[i])
        return res