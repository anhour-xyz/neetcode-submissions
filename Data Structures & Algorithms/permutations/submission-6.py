class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        visit = [False] * (len(nums))
        def dfs(i,cur):
            if len(cur) == len(nums):
                res.append(cur.copy())
                return
            for j in range(len(visit)):
                if not visit[j]:
                    visit[j] = True
                    cur.append(nums[j])
                    dfs(j+1,cur)
                    cur.pop()
                    visit[j] = False

        dfs(0,[])
        return res