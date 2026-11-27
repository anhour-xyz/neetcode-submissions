ROMAN = {
    "I": 1, "V": 5, "X": 10,
    "L": 50, "C": 100, "D": 500, "M": 1000
}

class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        for x,y in pairwise(s):
            x,y = ROMAN[x], ROMAN[y]
            res += x if x >= y else -x
        res += ROMAN[s[-1]]
        return res