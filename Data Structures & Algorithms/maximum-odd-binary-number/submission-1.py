class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        cnt_1 = 0
        cnt_0 = 0
        for i in s:
            if i == "1":
                cnt_1 += 1
            else:
                cnt_0 += 1
        res = ""
        if cnt_1 > 1:
            for i in range(cnt_1-1):
                res += "1"
            for j in range(cnt_0):
                res += "0"
            return res + "1"
        elif cnt_1 == 0: return s
        else:
            for i in range(cnt_0):
                res += "0"
            return res + "1"
