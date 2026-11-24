class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = set()
        map = defaultdict(int)
        for n in nums:
            map[n] += 1
            if map[n] > len(nums) / 3: res.add(n)
        return list(res)