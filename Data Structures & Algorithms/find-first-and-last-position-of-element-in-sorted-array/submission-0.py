class Solution:
    def find(self,nums,target):
        l,r = 0, len(nums) - 1
        while l <= r:
            mid = (l+r) // 2
            if nums[mid] >= target:
                r = mid - 1
            else:
                l = mid + 1
        return l


    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = self.find(nums,target)
        if start == len(nums) or nums[start] != target: return [-1,-1]
        end = self.find(nums,target+1) - 1
        return [start,end]