class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
        minHeap = []
        for key, val in count.items():
            heapq.heappush(minHeap,[val,key])
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        res = []
        while len(minHeap) > 0:
            res.append(heapq.heappop(minHeap)[1])
        return res