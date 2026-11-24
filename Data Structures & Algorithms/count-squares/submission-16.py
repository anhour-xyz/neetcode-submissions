class CountSquares:

    def __init__(self):
        self.points = []
        self.cnt = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.points.append(point)
        self.cnt[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        x1, y1 = point
        res = 0
        for x2,y2 in self.points:
            if x2 == x1 or y1 == y2 or abs(x1-x2) != abs(y1-y2):
                continue
            res += self.cnt[(x2,y1)] * self.cnt[(x1,y2)]
        return res
