class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        check = defaultdict(int)
        if len(nums) == 1: return False
        for i in range(k+1):
            if nums[i] in check: return True
            check[nums[i]] += 1

        for i in range(1,len(nums)-k):
            check[nums[i-1]] -= 1
            if check[nums[i-1]] == 0:
                del check[nums[i-1]]
            if nums[i+k] in check:
                return True
            check[nums[i+k]] += 1
        return False