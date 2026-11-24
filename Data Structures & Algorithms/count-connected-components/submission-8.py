class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        link = defaultdict(list)
        for n1,n2 in edges:
            link[n1].append(n2)
            link[n2].append(n1)
        visit = [False] * n
        def dfs(i):
            for n in link[i]:
                if not visit[n]:
                    visit[n] = True
                    dfs(n)
        cnt = 0
        for i in range(n):
            if not visit[i]:
                dfs(i)
                cnt += 1
        return cnt
        