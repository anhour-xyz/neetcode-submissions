class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        cnt = defaultdict(int)
        total = 0
        res = 0
        for n in nums:
            cnt[total] += 1
            total += n
            res += cnt[total-goal]
        return res