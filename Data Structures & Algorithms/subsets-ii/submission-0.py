class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        check = set()
        def dfs(i,cur):
            if i >= len(nums):
                if tuple(sorted(cur.copy())) not in check:
                    res.append(cur.copy())
                    check.add(tuple(sorted(cur.copy())))
                return

            cur.append(nums[i])
            dfs(i+1,cur)
            cur.pop()
            dfs(i+1,cur)

        dfs(0,[])
        return res