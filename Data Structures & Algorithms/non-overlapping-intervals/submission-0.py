class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])
        min_heap = []
        for interval in intervals:
            if min_heap and min_heap[0] <= interval[0]:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap,interval[1])
        if len(min_heap) == 1:
            return 0
        else:
            return len(intervals) - len(min_heap)
        


