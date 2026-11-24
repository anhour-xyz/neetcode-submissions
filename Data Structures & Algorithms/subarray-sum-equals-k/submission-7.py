class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = defaultdict(int)
        total = 0
        res = 0
        for n in nums:
            cnt[total] += 1
            total += n
            res += cnt[total-k]
        return res