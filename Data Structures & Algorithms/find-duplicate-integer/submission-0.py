class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        map = defaultdict(int)
        for n in nums:
            map[n] += 1
            if map[n] > 1: return n