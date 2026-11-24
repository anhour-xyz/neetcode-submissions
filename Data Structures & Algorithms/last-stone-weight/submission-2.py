class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = stones
        heapq.heapify_max(maxHeap)
        while len(maxHeap) >= 2:
            first = heapq.heappop(maxHeap)
            second = heapq.heappop(maxHeap)
            if abs(first-second) == 0:
                continue
            else:
                heapq.heappush(maxHeap,abs(first-second))
                heapq.heapify(maxHeap)
        return maxHeap[0]