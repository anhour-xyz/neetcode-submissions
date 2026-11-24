class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visit = set()
        start = [0,0]
        visit.add((0,0))
        for p in path:
            if p == "N":
                start[0] +=1
            elif p == "E":
                start[1] += 1
            elif p == "W":
                start[1] -= 1
            else:
                start[0] -= 1
            if (start[0],start[1]) in visit: return True
            visit.add((start[0],start[1]))
        return False