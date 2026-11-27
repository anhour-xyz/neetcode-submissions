class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pre = 0
        prefixSum = []
        for n in nums:
            prefixSum.append(pre)
            pre += n

        post = 0
        res = -1
        for i in range(len(nums)-1,-1,-1):
            if post == prefixSum[i]:
                res = i
            post += nums[i]
        return res 
            