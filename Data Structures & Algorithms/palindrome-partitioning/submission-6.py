class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def dfs(i,cur):
            if i >= len(s):
                res.append(cur.copy())
                return 
            for j in range(i,len(s)):
                t = s[i:j+1]
                if t == t[::-1]:
                    cur.append(t)
                    dfs(j+1,cur)
                    cur.pop()
        dfs(0,[])
        return res