class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        minHeap = []
        for stone in stones:
            minHeap.append(-stone)
        heapq.heapify(minHeap)
        while len(minHeap) > 1:
            first = heapq.heappop(minHeap)
            second = heapq.heappop(minHeap)
            heapq.heappush(minHeap,first-second)
        return -minHeap[0]
