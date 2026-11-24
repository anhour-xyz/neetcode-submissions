class Solution:
    def isHappy(self, n: int) -> bool:
        res = n
        visit = set()
        while res != 1:
            total = 0
            while res > 0:
                mod = res % 10
                total += mod ** 2
                res //= 10
            res = total 
            if total in visit: return False
            visit.add(total)
        return True

