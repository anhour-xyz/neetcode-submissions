class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l,r = max(weights), sum(weights)
        res = float('inf')
        while l <= r:
            mid = (l+r) // 2
            time = 0
            total = 0
            for w in weights:
                total += w
                if total >= mid:
                    time += 1
                    if total == mid:
                        total = 0
                    else:
                        total = w
            if total != 0: time += 1
            

            if time <= days:
                res = min(res,mid)
                r = mid - 1
            else:
                l = mid + 1
        return res
