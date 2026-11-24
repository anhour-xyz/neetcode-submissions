class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre = 0
        res = [0] * len(nums)
        cnt = 0
        for i in range(len(nums)):
            res[i] = pre
            pre += nums[i]
        check = [0] * len(nums)
        back = 0
        for i in range(len(nums)-1,-1,-1):
            check[i] = back
            back += nums[i]

        for i in range(len(res)):
            if not (res[i] == 2 and check[i] == 2):
                cnt += 1
        return cnt
        
        

        
