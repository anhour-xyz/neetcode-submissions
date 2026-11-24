class CountSquares:

    def __init__(self):
        self.point = []
        self.pointsCount = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.point.append(point)
        self.pointsCount[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        res = 0
        x,y = point
        for px,py in self.point:
            if abs(px-x) != abs(py-y) or x == px or y == py:
                continue
            res += self.pointsCount[(x,py)] * self.pointsCount[(px,y)]
        return res
            
        
