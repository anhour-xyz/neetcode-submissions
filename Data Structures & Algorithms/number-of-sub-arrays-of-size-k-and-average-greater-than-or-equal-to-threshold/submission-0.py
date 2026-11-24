class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        total = 0
        idx = 0
        for i in range(k):
            total += arr[idx]
            idx += 1

        cnt = 0
        if total / k >= threshold: cnt += 1
        for i in range(1,len(arr)-k+1):
            total -= arr[i-1]
            total += arr[i+k-1]
            if total / k >= threshold:
                cnt += 1
        return cnt