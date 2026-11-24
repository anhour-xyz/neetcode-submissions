class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        map = defaultdict(int)
        for n in nums:
            map[n] += 1
        res = 0
        for value in map.values():
            if value >= 2:
                res += math.factorial(value) // (2 * math.factorial(value-2))
        return res