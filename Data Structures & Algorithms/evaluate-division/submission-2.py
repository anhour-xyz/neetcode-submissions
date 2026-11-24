class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        map = defaultdict(list)
        for i in range(len(equations)):
            n = values[i]
            a,b = equations[i]
            map[a].append([b,n])
            map[b].append([a,1/n])
        
        def bfs(start,end):
            if start not in map or end not in map:
                return -1
            q, visit = deque(), set()
            q.append([start,1])
            visit.add(start)
            while q:
                n, w = q.popleft()
                if n == end: return w
                for nei, weight in map[n]:
                    if nei not in visit:
                        visit.add(nei)
                        q.append([nei,weight * w])
            return -1

        return [bfs(start,end) for start, end in queries]