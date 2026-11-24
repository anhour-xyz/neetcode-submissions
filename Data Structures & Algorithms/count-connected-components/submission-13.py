class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        map = defaultdict(list)
        for n1,n2 in edges:
            map[n1].append(n2)
            map[n2].append(n1)
        res = 0
        visit = [False] * (n)

        def dfs(i):
            for nei in map[i]:
                if visit[nei] == False:
                    visit[nei] = True
                    dfs(nei)

        for i in range(n):
            if visit[i] == False:
                dfs(i)
                res += 1
        return res