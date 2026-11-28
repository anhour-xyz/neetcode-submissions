class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        pre = 0
        prefix = []
        for n in nums:
            pre += n
            prefix.append(pre)
           

        post = nums[-1]
        res = 0
        for i in range(len(nums)-2,-1,-1):
            if post == prefix[i]:
                res += 1
            post += nums[i]
        return res
