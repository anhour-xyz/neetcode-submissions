class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        res = []
        if len(intervals) == 1: return intervals
        if len(intervals) == 2:
            if intervals[1][0] <= intervals[0][1]: return [[intervals[0][0], max(intervals[0][1],intervals[1][1])]]
            else:
                return intervals
        j = 0
        while j < len(intervals) - 1:
            temp = intervals[j]
            i = j+1
            while i < len(intervals) and intervals[i][0] <= temp[1]:
                temp[1] = max(temp[1],intervals[i][1])
                i += 1
            i -= 1
            if i == j:
                res.append(intervals[i])
            else:
                res.append(temp)
            j = i + 1
        if intervals[-1][0] <= res[-1][1]:
            res[-1][1] = max(res[-1][1],intervals[-1][1])
        else:
            res.append(intervals[-1])
        return res