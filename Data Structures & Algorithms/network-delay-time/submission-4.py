class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)
        for u,v,e in times:
            edges[u].append([v,e])
        
        visit = set()
        res = 1
        minHeap = [[0,k]]

        while minHeap:
            w1,n1 = heapq.heappop(minHeap)
            if n1 in visit: continue
            visit.add(n1)
            res = w1
            for n2,w2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap,(w1+w2,n2))
        return res if len(visit) == n else -1


