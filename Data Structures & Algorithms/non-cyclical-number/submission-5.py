class Solution:
    def isHappy(self, n: int) -> bool:
        total = n
        visit = set()
        while total != 1:
            copy = total
            temp = 0
            while copy > 0:
                mod = copy % 10
                temp += mod
                copy //= 10
            if temp in visit: return False
            else:
                visit.add(temp)
                total = temp
        return True
            
