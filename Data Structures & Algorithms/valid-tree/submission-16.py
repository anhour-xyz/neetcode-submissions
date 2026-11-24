class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visit = set()
        map = defaultdict(list)
        for a,b in edges:
            map[a].append(b)
            map[b].append(a)

        def dfs(n,preRoot):
            if n in visit: return False
            visit.add(n)
            for nei in map[n]:
                if nei == preRoot: continue
                if not dfs(nei,n): return False
            return True
        

        return dfs(0,-1) and len(visit) == n