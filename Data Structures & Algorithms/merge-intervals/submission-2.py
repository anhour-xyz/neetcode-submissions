class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        i = 1
        res = [intervals[0]]
        while i < len(intervals):
            cur = intervals[i]
            if cur[0] <= res[-1][1]:
                res[-1][1] = max(res[-1][1], cur[1])
            else:
                res.append(cur)
            i += 1
        return res


