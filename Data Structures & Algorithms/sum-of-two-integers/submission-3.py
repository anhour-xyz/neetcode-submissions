class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFF
        MAX = 0x7FFFFF
        while b!=0:
            c = (a&b)<<1
            a = (a^b) & mask
            b = c&mask
        return a if a<=MAX else ~(a^mask)