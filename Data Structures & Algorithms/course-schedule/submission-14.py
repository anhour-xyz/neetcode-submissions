class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = defaultdict(list)
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        visit = set()
        def dfs(n):
            if n in visit: return False
            if preMap[n] == []: return True
            visit.add(n)
            for pre in preMap[n]:
                if not dfs(pre): return False
            visit.remove(n)
            preMap[n] = []
            return True
            
        for n in range(numCourses):
            if not dfs(n): return False
        return True

        