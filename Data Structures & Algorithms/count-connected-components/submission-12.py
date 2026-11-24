class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        connect = defaultdict(list)
        for u,v in edges:
            connect[u].append(v)
            connect[v].append(u)

        visit = [False] * n

        def dfs(i):
            for nei in connect[i]:
                if not visit[nei]:
                    visit[nei] = True
                    dfs(nei)
        res = 0
        for i in range(n):
            if not visit[i]:
                dfs(i)
                res += 1
        return res 