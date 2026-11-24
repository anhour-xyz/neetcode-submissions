"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x:x.end)
        res = 1
        preMax = intervals[0].end
        for i in range(1,len(intervals)):
            if intervals[i].start < preMax:
                continue
            else:
                preMax = intervals[i].end
                res += 1
        return res