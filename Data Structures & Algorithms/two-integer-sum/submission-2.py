class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(nums)):
            t = target - nums[i]
            if t in map: return [map[t],i]
            map[nums[i]] = i
        