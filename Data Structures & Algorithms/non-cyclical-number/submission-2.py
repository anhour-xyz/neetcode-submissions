class Solution:
    def isHappy(self, n: int) -> bool:
        temp = n
        total = 0
        check = set()
        while total != 1:
            total = 0
            while temp > 0:
                mod = temp % 10
                temp //= 10
                total += mod ** 2
            if total in check: return False
            elif total == 1: return True
            temp = total
            check.add(total)
        return True

        
