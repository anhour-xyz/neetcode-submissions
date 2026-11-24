class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visit = [False] * len(isConnected)

        res = 0

        def dfs(i):
            visit[i] = True
            for j in range(len(isConnected)):
                if not visit[j] and isConnected[i][j] == 1:
                    dfs(j)

        for i in range(len(isConnected)):
            if not visit[i]:
                dfs(i)
                res += 1
        return res