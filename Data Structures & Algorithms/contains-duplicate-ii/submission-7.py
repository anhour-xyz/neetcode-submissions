class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k + 1> len(nums):
            k = min(k+1, len(nums))
        else:
            k = k + 1
        check = defaultdict(int)

        for i in range(k):
            if nums[i] in check: return True
            check[nums[i]] += 1
        
        for i in range(1,len(nums)-k+1):
            check[nums[i-1]] -= 1
            if check[nums[i-1]] == 0:
                del check[nums[i-1]]
            if check[nums[i+k-1]] in check: return True
            check[nums[i+k-1]] += 1
        return False
