class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pre = 0
        res = []
        for n in nums:
            res.append(pre)
            pre += n

        post = 0
        for i in range(len(nums)-1,-1,-1):
            temp = post
            if temp == res[i]: return i
            post += nums[i]
        return -1
