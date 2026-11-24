class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        temp = sorted(nums)
        if temp == nums: return True
        elif nums == temp[::-1]: return True
        else: return False