class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[0])
        result = [intervals[0]]
        for i in range(1,len(intervals)):
            first = result[-1]
            second = intervals[i]
            if first[0] < second[1] and second[0] < first[1]:
                continue
            result.append(second)

        return len(intervals) - len(result)