class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for n1,n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        count = 0
        visit = [False] * n

        def dfs(n):
            for nei in adj[n]:
                if not visit[nei]:
                    visit[nei] = True
                    dfs(nei)
        
        for i in range(n):
            if not visit[i]:
                dfs(i)
                count += 1
        return count