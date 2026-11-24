class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        map = {
            "0":0,
            "1":1,
            "2":2,
            "3":3,
            "4":4,
            "5":5,
            "6":6,
            "7":7,
            "8":8,
            "9":9
        }

        total1, total2 = 0,0
        j = len(num1) - 1
        k = len(num2) - 1
        for n in num1:
            total1 += map[n] * (10 ** j)
            j -= 1
        
        for n in num2:
            total2 += map[n] * (10 **k)
            k -= 1
        
        product = total1 * total2
        return str(product)