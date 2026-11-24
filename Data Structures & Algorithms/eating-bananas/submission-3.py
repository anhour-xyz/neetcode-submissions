class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)
        res = float('inf')
        while l <= r:
            mid = (l+r) // 2
            time = 0
            for p in piles:
                if p % mid == 0:
                    time += p // mid
                else:
                    time += p // mid + 1
            if time <= h:
                res = min(res,mid)
                r = mid - 1
            else:
                l = mid + 1
        return res
                
