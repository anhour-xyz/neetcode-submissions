class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        map = defaultdict(list)
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i+1,len(points)):
                x2, y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                map[i].append([dist,j])
                map[j].append([dist,i])

        minHeap = [[0,0]]
        visit = set()
        res = 0
        while minHeap:
            c,n = heapq.heappop(minHeap)
            if n in visit: continue
            visit.add(n)
            res += c
            for c1,n2 in map[n]:
                if n2 not in visit:
                    heapq.heappush(minHeap,[c1,n2])
        return res
