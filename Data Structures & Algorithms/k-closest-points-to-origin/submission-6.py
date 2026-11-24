class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for x, y in points:
            dist = x ** 2 + y ** 2
            heapq.heappush(minHeap, [-dist,x,y])
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        res = []
        while minHeap:
            res.append(heapq.heappop(minHeap)[1:])

        return res