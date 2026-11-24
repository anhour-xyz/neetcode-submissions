class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        if not self.large or num > self.large[0]:
            heapq.heappush(self.large,num)
        else:
            heapq.heappush(self.small,-num)
        
        if len(self.small) + 1 < len(self.large):
            num = heapq.heappop(self.large)
            heapq.heappush(self.small,-num)
        if len(self.large) + 1 < len(self.small):
            num = heapq.heappop(self.small)
            heapq.heappush(self.small,-num)

    def findMedian(self) -> float:
        if len(self.large) == len(self.small):
            return (self.large[0] -self.small[0]) / 2.0
        if len(self.large) > len(self.small):
            return self.large[0]
        else:
            return -self.small[0]
        
        