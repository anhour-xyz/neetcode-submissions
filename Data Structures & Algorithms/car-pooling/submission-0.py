class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        minHeap = []
        for n,s,e in trips:
            heapq.heappush(minHeap,[s,e,n])
        cur_des = -1
        while len(minHeap) > 0:
            s,e,n = heapq.heappop(minHeap)
            if n > capacity: return False
            if s < cur_des: return False
            cur_des = e

        return True
