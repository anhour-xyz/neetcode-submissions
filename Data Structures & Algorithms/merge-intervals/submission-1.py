class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1: return intervals

        intervals.sort(key=lambda x:x[0])
        i = 1
        temp = intervals[0]
        res = []

        while i < len(intervals):
            if intervals[i][0] > temp[1]:
                res.append(temp)
                temp = intervals[i]
                i += 1
            else:
                while i < len(intervals) and intervals[i][0] <= temp[1]:
                    temp = [temp[0], max(intervals[i][1], temp[1])]
                    i += 1
                res.append(temp)
                if i < len(intervals):
                    temp = intervals[i]
                i += 1

            if i == len(intervals): 
                res.append(temp)
        return res
