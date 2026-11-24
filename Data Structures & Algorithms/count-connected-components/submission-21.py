class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visit = [False] * (n)
        map = defaultdict(list)
        for a, b in edges:
            map[a].append(b)
            map[b].append(a)
        res = 0

        def dfs(i):
            visit[i] = True
            for nei in map[i]:
                if not visit[nei]:
                    dfs(nei)
            return

        for i in range(n):
            if not visit[i]:
                dfs(i)
                res += 1
        return res