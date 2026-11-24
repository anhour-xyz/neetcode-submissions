class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        map = defaultdict(int)
        for n in nums:
            map[n] += 1
            if map[n] > len(nums) / 2:
                return n