class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pre = 0
        res = []
        for n in nums:
            res.append(pre)
            pre += n
        ans = float('inf')
        post = 0
        for i in range(len(nums)-1,-1,-1):
            temp = post
            if temp == res[i]:
                ans = min(ans,i)
            post += nums[i]
        return ans if ans != float('inf') else -1
