class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        map = defaultdict(list)
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i+1,len(points)):
                x2, y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                map[j].append([dist,i])
                map[i].append([dist,j])

        visit = set()
        res = 0
        minHeap = [[0,0]]

        while len(visit) < n:
            cost, i = heapq.heappop(minHeap)
            if i in visit: continue
            visit.add(i)
            res += cost
            for cost, nei in map[i]:
                if nei not in visit:
                    heapq.heappush(minHeap,[cost,nei])

        return res
