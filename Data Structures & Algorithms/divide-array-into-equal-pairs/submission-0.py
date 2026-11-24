class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        if len(nums) % 2 != 0: return False
        map = defaultdict(int)
        for n in nums:
            map[n] += 1
        for value in map.values():
            if value % 2 != 0:
                return False
        return True
