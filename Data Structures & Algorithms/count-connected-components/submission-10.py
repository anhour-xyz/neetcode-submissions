class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        connect = defaultdict(list)
        for n1,n2 in edges:
            connect[n1].append(n2)
            connect[n2].append(n1)
        
        visit = [False] * n

        def dfs(n):
            for nei in connect[n]:
                if not visit[nei]:
                    visit[nei] = True
                    dfs(nei)

        res = 0

        for i in range(n):
            if not visit[i]:
                dfs(i)
                res += 1

        return res
