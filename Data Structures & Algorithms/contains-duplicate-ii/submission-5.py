class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) == 1: return False
        map = defaultdict(int)
        k += 1
        for i in range(k):
            if nums[i] in map: return True
            map[nums[i]] += 1
        
        for i in range(1,len(nums)-k+1):
            map[nums[i-1]] -= 1
            if map[nums[i-1]] == 0:
                del map[nums[i-1]]
            
            if nums[i+k-1] in map: return True
            map[nums[i+k-1]] += 1
        return False
