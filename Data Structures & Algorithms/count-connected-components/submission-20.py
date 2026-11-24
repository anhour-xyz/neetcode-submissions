class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        map = defaultdict(list)
        for n1, n2 in edges:
            map[n1].append(n2)
            map[n2].append(n1)

        visit = [False] * n
        res = 0

        def dfs(n):
            visit[n] = True
            for nei in map[n]:
                if not visit[nei]:
                    dfs(nei)

        for i in range(n):
            if not visit[i]:
                dfs(i)
                res += 1
        return res