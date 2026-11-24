class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        if not self.large or num > self.large[0]:
            heapq.heappush(self.large,num)
        else:
            heapq.heappush(self.small,-num)

        if len(self.large) > len(self.small) + 1:
            n = heapq.heappop(self.large)
            heapq.heappush(self.small,-n)
        
        if len(self.small) > len(self.large) + 1:
            n = heapq.heappop(self.small)
            heapq.heappush(self.large,-n)

    def findMedian(self) -> float:
        if len(self.large) == len(self.small):
            return (self.large[0] + (-1 * self.small[0])) / 2.0
        elif len(self.large) > len(self.small):
            return self.large[0]
        else:
            return self.small[0] * -1
        
        