class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        total = 0
        cur_time = 0
        for cus in customers:
            cur_time = max(cur_time, cus[0]) + cus[1]
            total += cur_time - cus[0]
        return total / len(customers)