class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        check = [False] * len(nums)
        res = []
        def dfs(i,cur):
            if len(cur) == len(nums):
                res.append(cur.copy())
                return

            for j, c in enumerate(check):
                if not c:
                    cur.append(nums[j])
                    check[j] = True
                    dfs(j+1,cur)
                    cur.pop()
                    check[j] = False
        dfs(0,[])
        return res
            
