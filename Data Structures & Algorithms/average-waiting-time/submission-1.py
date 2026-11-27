class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        total = 0
        cur_time = 0
        for start, time in customers:
            cur_time = max(cur_time, start) + time
            total += cur_time - start 
        return total / len(customers)