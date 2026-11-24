class Solution:
    def isHappy(self, n: int) -> bool:
        temp = n
        check = set()
        while temp != 1:
            total = 0
            while temp > 0:
                mod = temp % 10
                temp = temp // 10
                total +=  mod ** 2
            if total in check: return False
            else: check.add(total)
            temp = total
        
        return True