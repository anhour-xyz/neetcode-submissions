class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [nums[0]] * len(nums)
        postfix = [nums[len(nums)-1]] * len(nums)
        for i in range(1,len(nums)):
            prefix[i] = nums[i] * prefix[i-1]
        for j in range(len(nums)-2,-1,-1):
            postfix[j] = nums[j] * postfix[j+1]
        res = []
        for i in range(len(nums)):
            temp = 1
            if i == 0:
                temp *= postfix[i+1]
            elif i == len(nums) - 1:
                temp *= prefix[i-1]
            else:
                temp *= prefix[i-1] * postfix[i+1]
            res.append(temp)
        return res
