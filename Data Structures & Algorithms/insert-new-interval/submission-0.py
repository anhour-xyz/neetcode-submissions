class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        if len(intervals) == 1:
            if newInterval[0] > intervals[0][1]:
                res.append(intervals[0])
                res.append(newInterval)
            else:
                res.append(intervals[0], max(newInterval[1], intervals[0][1]))
            return res

        for i in range(1,len(intervals)):
            if newInterval[0] > intervals[i][1] and newInterval[0] > intervals[i-1][1]:
                res.append(intervals[i-1])
                res.append(intervals[i])
            elif newInterval[1] < intervals[i-1][0]:
                res.append(intervals[i-1])
            elif newInterval[0] > intervals[i-1][1] and newInterval[1] < intervals[i][0]:
                res.append(newInterval)
            elif newInterval[0] > intervals[i-1][1] and newInterval[0] < intervals[i][1] and newInterval[0] > intervals[i][0]:
                res.append([newInterval[0], max(newInterval[1], intervals[i][1])])
            elif newInterval[0] <= intervals[i-1][1] and newInterval[1] >= intervals[i][0]:
                res.append([intervals[i-1][0], max(newInterval[1],intervals[i][1])])
            elif newInterval[0] <= intervals[i-1][1] and newInterval[1] < intervals[i][0]:
                res.append([intervals[i-1][0], newInterval[1]])
        if res[-1][1] < intervals[-1][0]:
            res.append(intervals[-1])
        return res
