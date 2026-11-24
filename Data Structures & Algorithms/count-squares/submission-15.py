class CountSquares:

    def __init__(self):
        self.points = []
        self.point_cnt = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.points.append(point)
        self.point_cnt[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        total = 0
        x1, y1 = point
        for x2,y2 in self.points:
            if x1 == x2 or y1 == y2 or abs(x1-x2) != abs(y1-y2):
                continue
            total += self.point_cnt[(x1,y2)] * self.point_cnt[(x2,y1)]
        return total
        
