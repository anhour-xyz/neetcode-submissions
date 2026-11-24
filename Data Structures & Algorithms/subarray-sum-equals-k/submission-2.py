class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = defaultdict(int)
        ans = s = 0
        for n in nums:
            cnt[s] += 1
            s += n
            ans += cnt[s-k]
        return ans

