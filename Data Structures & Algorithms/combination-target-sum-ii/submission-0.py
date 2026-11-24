class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        check = set()
        def dfs(i,cur,total):
            if total == target:
                if tuple(cur.copy()) not in check:
                    res.append(cur.copy())
                    check.add(tuple(cur.copy()))
                return
            if i >= len(candidates):
                return

            cur.append(candidates[i])
            dfs(i+1,cur,total+candidates[i])
            cur.pop()
            dfs(i+1,cur,total)

        dfs(0,[],0)
        return res