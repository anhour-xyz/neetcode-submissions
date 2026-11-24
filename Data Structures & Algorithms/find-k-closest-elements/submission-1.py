class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        minDiff = float('inf')
        res = [0,0]
        diff = 0
        for i in range(k):
            diff += abs(arr[i]-x)
        if diff < minDiff:
            minDiff = diff
            res = [0,k-1]
        
        for i in range(1,len(arr)-k+1):
            temp = abs(arr[i-1]-x)
            diff -= temp
            diff += abs(arr[i+k-1]-x)
            if diff < minDiff:
                minDiff = diff
                res = [i,i+k-1]
        
        return arr[res[0]:res[1]+1]