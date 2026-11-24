class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i, n in enumerate(nums):
            t = target - n
            if t in map: return [map[t], i]
            map[n] = i