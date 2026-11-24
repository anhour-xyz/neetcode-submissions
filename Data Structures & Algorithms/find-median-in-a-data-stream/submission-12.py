class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        if not self.large or num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -num)
        
        if 1 + len(self.large) < len(self.small):
            n = heapq.heappop(self.small)
            heapq.heappush(self.large,-n)
        
        if 1 + len(self.small) < len(self.large):
            n = heapq.heappop(self.large)
            heapq.heappush(self.small,-n)

    def findMedian(self) -> float:
        
        if len(self.small) == len(self.large):
            return (self.large[0] + -self.small[0]) / 2.0
        elif len(self.small) > len(self.large):
            return -self.small[0]
        else:
            return self.large[0]
        