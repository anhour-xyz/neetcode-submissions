class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        connect = defaultdict(list)
        for n1, n2 in edges:
            connect[n1].append(n2)
            connect[n2].append(n1)

        visit = set()

        def dfs(n,pre):
            if n in visit: return False
            visit.add(n)
            for nei in connect[n]:
                if nei == pre: continue
                if not dfs(nei,n): return False
            return True

        return dfs(0,-1) and len(visit) == n