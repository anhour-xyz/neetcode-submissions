class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        connect = defaultdict(list)
        for n1,n2 in edges:
            connect[n1].append(n2)
            connect[n2].append(n1)

        visit = set()
        def dfs(root,prev):
            if root in visit: return False
            visit.add(root)
            for l in connect[root]:
                if l == prev: continue
                if not dfs(l,root): return False
            return True




        return dfs(0,-1) and len(visit) == n