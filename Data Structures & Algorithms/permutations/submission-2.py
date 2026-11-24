class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        check = [False] * len(nums)

        def dfs(i,cur):
            if len(cur) == len(nums):
                res.append(cur.copy())
                return
            for j, on in enumerate(check):
                if not on:
                    cur.append(nums[j])
                    check[j] = True
                    dfs(i,cur)
                    check[j] = False
                    cur.pop()
        dfs(0,[])
        return res