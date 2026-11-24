class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        total = 0
        map = defaultdict(int)
        check = True
        res = 0
        for i in range(k):
            if nums[i] in map:
                check = False
            map[nums[i]] += 1
            total += nums[i]

        if check: res = max(res,total)

        for i in range(1,len(nums)-k+1):
            check = True
            map[nums[i-1]] -= 1
            if map[nums[i-1]] == 0: del map[nums[i-1]]
            if nums[i+k-1] in map:
                check = False
            total -= nums[i-1]
            total += nums[i+k-1]
            if check: res = max(res,total)
        return res 

