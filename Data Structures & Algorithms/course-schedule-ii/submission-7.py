class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = defaultdict(list)
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        res = []
        visit, cycle = set(), set()
        def dfs(n):
            if n in cycle: return False
            if n in visit: return True
            cycle.add(n)
            for pre in preMap[n]:
                if not dfs(pre): return False
            cycle.remove(n)
            visit.add(n)
            res.append(n)
            return True
        
        for i in range(numCourses):
            if not dfs(i): return []
        return res