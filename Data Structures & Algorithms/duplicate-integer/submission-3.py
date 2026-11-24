class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map = defaultdict(int)
        for n in nums:
            map[n] += 1
        for key, value in map.items():
            if value != 1: return True
        return False