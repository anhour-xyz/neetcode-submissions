class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x:x[1])
        curPass = 0
        minHeap = []
        for numPass, start, end in trips:
            while minHeap and start >= minHeap[0][0]:
                curPass -= heapq.heappop(minHeap)[1]
            curPass += numPass
            if curPass > capacity: return False
            heapq.heappush(minHeap,[end,numPass])
        return True