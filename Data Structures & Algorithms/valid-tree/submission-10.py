class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for n1,n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visit = set()

        def dfs(n, preNode):
            if n in visit: return False
            visit.add(n)
            for nei in adj[n]:
                if nei == preNode: continue
                if not dfs(nei,n): return False
            return True

        return dfs(0,-1) and len(visit) == n