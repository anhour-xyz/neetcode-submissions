class Solution:
    def check(self, nums: List[int]) -> bool:
        copy = sorted(nums.copy())
        for i in range(len(nums)):
            temp = copy[i:] + copy[:i]
            if temp == nums: return True
        return False