class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        link = defaultdict(list)
        for n1,n2 in edges:
            link[n1].append(n2)
            link[n2].append(n1)
        
        visit = [False] * n
        res = 0

        def dfs(i):
            for n in link[i]:
                if not visit[n]:
                    visit[n] = True
                    dfs(n)

        for i in range(n):
            if not visit[i]:
                dfs(i)
                res += 1
        return res