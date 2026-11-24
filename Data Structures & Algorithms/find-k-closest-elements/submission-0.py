class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        max_dif, min_dif = max(abs(x-arr[0]),abs(x-arr[k-1])), min(abs(x-arr[0]),abs(x-arr[k-1]))
        res = arr[:k]
        for i in range(1,len(arr)-k+1):
            if max(abs(arr[i]-x),abs(arr[i+k-1] - x)) < max_dif and  min(abs(arr[i] - x),abs(arr[i+k-1] - x)) < min_dif:
                res = arr[i:i+k]
                max_dif = abs(arr[i] - x)
                min_dif = abs(arr[i+k-1] - x)
        return res
            

