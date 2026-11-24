class CountSquares:

    def __init__(self):
        self.points = []
        self.pointscnt = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.pointscnt[tuple(point)] += 1
        self.points.append(point)

    def count(self, point: List[int]) -> int:
        res = 0
        x, y = point
        for px,py in self.points:
            if abs(px-x) != abs(py-y) or x == px or y == py: 
                continue
            res += self.pointscnt[(x,py)] * self.pointscnt[(px,y)]
        return res
