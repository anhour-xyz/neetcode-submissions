class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        minDiff = float('inf')
        total = 0
        for i in range(k):
            total += abs(x-arr[i])
        minDiff = total
        res = [0,k]
        for i in range(1,len(arr)-k+1):
            total -= abs(x-arr[i-1])
            total += abs(x-arr[i+k-1])
            if total < minDiff:
                minDiff = total
                res[0] = i
                res[1] = i+k
        return arr[res[0]:res[1]]