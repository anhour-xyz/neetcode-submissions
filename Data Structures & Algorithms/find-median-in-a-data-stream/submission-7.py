class MedianFinder:

    def __init__(self):
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        if self.large and num > self.large[0]:
            heapq.heappush(self.large,num)
        else:
            heapq.heappush(self.small,-num)

        if len(self.large) > len(self.small) + 1:
            num = heapq.heappop(self.large)
            heapq.heappush(self.small,num * -1)
        elif len(self.small) > len(self.large) + 1:
            num = heapq.heappop(self.small)
            heapq.heappush(self.large,num * -1)
        
    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return (self.small[0] * -1 + self.large[0]) / 2.0
        elif len(self.small) > len(self.large):
            return self.small[0] * -1
        else:
            return self.large[0] 
        
        