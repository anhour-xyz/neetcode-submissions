class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        map = defaultdict(int)
        for n in nums:
            map[n] += 1
        for key, val in map.items():
            if val % 2:
                return False
        return True