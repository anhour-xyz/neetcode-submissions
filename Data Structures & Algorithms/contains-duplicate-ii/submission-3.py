class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        check = set()
        for i in range(k):
            if nums[i] in check: return True
            check.add(nums[i])
        for i in range(1,len(nums)-k+1):
            if nums[i+k-1] in check: return True
            if nums[i-1] in check:
                check.remove(nums[i-1])
        return False