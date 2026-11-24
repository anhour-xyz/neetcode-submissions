class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        minHeap = []
        map = defaultdict(int)
        for n in nums:
            map[n] += 1
        for key, val in map.items():
            heapq.heappush(minHeap,[val,key])
            if len(minHeap) > k:
                heapq.heappop(minHeap)

        res = []
        while len(minHeap) > 0:
            res.append(heapq.heappop(minHeap)[1])
        return res
        