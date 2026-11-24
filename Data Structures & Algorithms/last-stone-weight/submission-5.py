class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-stone for stone in stones]
        heapq.heapify(maxHeap)
        while len(maxHeap) >= 2:
            first = heapq.heappop(maxHeap)
            second = heapq.heappop(maxHeap)
            heapq.heappush(maxHeap,first-second)
            heapq.heapify(maxHeap)
        return abs(maxHeap[0])