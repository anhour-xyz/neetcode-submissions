class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = defaultdict(list)
        for i in range(n):
            x1,y1 = points[i]
            for j in range(i+1,n):
                x2,y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                adj[i].append([dist,j])
                adj[j].append([dist,i])

        visit = set()
        res = 0
        minHeap = [[0,0]]

        while len(visit) < n:
            cost,point = heapq.heappop(minHeap)
            if point in visit: continue
            res += cost
            visit.add(point)
            for cost,i in adj[point]:
                if i not in visit:
                    heapq.heappush(minHeap,[cost,i])
        return res