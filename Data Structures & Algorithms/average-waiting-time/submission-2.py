class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        total = 0
        curTime = 0
        for start, time in customers:
            curTime = max(curTime,start) + time
            total += curTime - start
        return total / len(customers)