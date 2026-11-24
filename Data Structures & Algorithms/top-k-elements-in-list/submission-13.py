class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = defaultdict(int)
        for n in nums:
            map[n] += 1
        minHeap = []
        for key, val in map.items():
            heapq.heappush(minHeap,[val,key])
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        res = []
        while minHeap:
            res.append(heapq.heappop(minHeap)[1])
        return res