class Solution:
    def getSum(self, a: int, b: int) -> int:
        c_in = 0
        s = 0
        mask = 0xFFFFFFFF

        for i in range(32):
            one = 1 & (a >> i)
            two = 1 & (b >> i)
            new_place = one^two^c_in
            s = s | (new_place << i)
            c_in = one & two | one & c_in | two & c_in
        
        if s > 0x7FFFFFFF:
            s = ~(s ^ mask)

        return s