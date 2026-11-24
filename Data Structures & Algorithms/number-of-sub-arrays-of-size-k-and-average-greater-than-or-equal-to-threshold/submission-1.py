class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        total = 0
        res = 0
        for i in range(k):
            total += arr[i]

        if total / k >= threshold: res += 1
        for i in range(1,len(arr)-k+1):
            total -= arr[i-1]
            total += arr[i+k-1]
            if total / k >= threshold:
                res += 1
        return res