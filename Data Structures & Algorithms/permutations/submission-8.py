class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        check = [False] * len(nums)
        res = []
        def dfs(i,cur):
            if len(cur) == len(nums):
                res.append(cur.copy())
                return 
            for j in range(len(check)):
                if not check[j]:
                    check[j] = True
                    cur.append(nums[j])
                    dfs(j+1,cur)
                    check[j] = False
                    cur.pop()
        dfs(0,[])
        return res