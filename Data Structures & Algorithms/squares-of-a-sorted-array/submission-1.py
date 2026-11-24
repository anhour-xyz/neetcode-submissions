class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        minimum = float('inf')
        for i, n in enumerate(nums):
            if abs(n) < minimum:
                minimum = abs(n)
                idx = i
        res = []
        res.append(nums[idx] ** 2)
        l = idx - 1
        r = idx + 1
        while l >= 0 and r < len(nums):
            if abs(nums[l]) <= abs(nums[r]):
                res.append(nums[l] ** 2)
                l -= 1
            else:
                res.append(nums[r] ** 2)
                r += 1
        if l == -1:
            for i in range(r,len(nums)):
                res.append(nums[i] ** 2)
        else:
            for i in range(l,-1,-1):
                res.append(nums[i] ** 2)
        return res

        
            
