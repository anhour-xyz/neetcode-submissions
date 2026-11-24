class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        adj = defaultdict(int)
        for src, dst in trust:
            adj[dst] += 1
            adj[src] -= 1
        for i in range(1,n+1):
            if adj[i] == n - 1: return i
        return -1
