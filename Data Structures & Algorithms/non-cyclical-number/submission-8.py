class Solution:
    def isHappy(self, n: int) -> bool:
        temp = n
        visit = set()
        while temp != 1:
            total = 0
            while temp > 0:
                mod = temp % 10
                total += mod ** 2 
                temp //= 10
            if total in visit:
                return False
            else:
                visit.add(total)
                temp = total
        return True