class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        def check(largest):
            total = 0
            subarray = 0
            for n in nums:
                total += n
                if total > largest:
                    subarray += 1
                    total = n
            return subarray + 1 <= k


        l, r = max(nums), sum(nums)
        res = r
        while l <= r:
            mid = (l+r) // 2
            if check(mid):
                res = min(res,mid)
                r = mid - 1
            else:
                l = mid + 1
        return res