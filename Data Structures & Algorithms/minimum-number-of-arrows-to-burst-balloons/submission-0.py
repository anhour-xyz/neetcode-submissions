class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])
        res = 1
        preMax = points[0][1]
        for i in range(1,len(points)):
            if points[i][0] <= preMax:
                continue
            else:
                res += 1
                preMax = points[i][1]
        return res
