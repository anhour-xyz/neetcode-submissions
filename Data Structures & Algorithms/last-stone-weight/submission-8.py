class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        minHeap = []
        for s in stones:
            heapq.heappush(minHeap,-s)
        while len(minHeap) > 1:
            first = heapq.heappop(minHeap)
            second = heapq.heappop(minHeap)
            diff = first - second
            heapq.heappush(minHeap,diff)
        return -minHeap[0]

