class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        map1 = {
            '0':0,
            '1':1,
            '2':2,
            '3':3,
            '4':4,
            '5':5,
            '6':6,
            '7':7,
            '8':8,
            '9':9
        }

        len1 = len(num1)
        len2 = len(num2)

        int1 = 0
        int2 = 0
        for i in range(len1):
            int1 += 10 ** (len1 - 1) * map1[num1[i]]
            len1 -= 1

        for j in range(len2):
            int2 += 10 ** (len2 - 1) * map1[num2[j]]
            len2 -= 1

        product = int1 * int2
        if product == 0: return '0'
        res = ''
        while product > 0:
            mod = product % 10
            product = product // 10
            res+= next(k for k, v in map1.items() if v == mod)
        return res[::-1]
