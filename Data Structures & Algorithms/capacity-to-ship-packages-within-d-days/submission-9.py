class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l,r = max(weights), sum(weights)
        res = r
        while l <= r:
            mid = (l+r) // 2
            time = 0
            total = 0
            for w in weights:
                if total + w < mid:
                    total += w
                else:
                    if total + w == mid:
                        total = 0
                    else:
                        total = w
                    time += 1
            if total: time += 1
            if time <= days:
                res = min(res,mid)
                r = mid - 1
            else:
                l = mid + 1
        return res