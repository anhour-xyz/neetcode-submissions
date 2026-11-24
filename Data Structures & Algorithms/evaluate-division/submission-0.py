class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        map = defaultdict(list)
        for i in range(len(equations)):
            n = values[i]
            a,b = equations[i]
            map[a].append([b,n])
            map[b].append([a,1/n])
        
        def bfs(src,target):
            if src not in map or target not in map: return -1
            q, visit = deque(), set()
            q.append([src,1])
            visit.add(src)
            while q:
                n, w = q.popleft()
                if n == target: return w
                for nei,weight in map[n]:
                    if nei not in visit:
                        q.append([nei, w * weight])
                        visit.add(nei)
            return -1

        return [bfs(start,end) for start, end in queries]