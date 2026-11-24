class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        link = defaultdict(list)
        for n1,n2 in edges:
            link[n1].append(n2)
            link[n2].append(n1)

        visit = [False] * n
        res = 0
        def dfs(node):

            for i in link[node]:
                if not visit[i]:
                    visit[i] = True
                    dfs(i)

        for node in range(n):
            if not visit[node]:
                dfs(node)
                res += 1
        return res