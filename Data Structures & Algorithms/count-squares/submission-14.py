class CountSquares:

    def __init__(self):
        self.ptsCount = defaultdict(int)
        self.pts = []

    def add(self, point: List[int]) -> None:
        self.ptsCount[(point[0],point[1])] += 1
        self.pts.append(point)

    def count(self, point: List[int]) -> int:
        x1, y1 = point[0], point[1]
        res = 0
        for x2, y2 in self.pts:
            if abs(x1-x2) != abs(y2-y1) or x2 == x1 or y1 == y2: continue
            res += self.ptsCount[(x1,y2)] * self.ptsCount[(x2,y1)]
        return res

        
