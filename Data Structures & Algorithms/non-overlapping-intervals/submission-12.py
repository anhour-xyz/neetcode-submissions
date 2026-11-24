class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        res = intervals[0][1]
        cnt = 1
        for i in range(1,len(intervals)):
            if intervals[i][0] < res:
                continue
            cnt += 1
            res = intervals[i][1]
        return len(intervals) - cnt