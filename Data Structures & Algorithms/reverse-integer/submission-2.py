class Solution:
    def reverse(self, x: int) -> int:
        Max_Int = 2**31 -1
        Min_Int = -2**31



        sign = -1 if x < 0 else 1
        x = abs(x)

        rev = 0

        while x != 0:
            digit = x % 10
            rev = rev * 10 + digit
            x = x // 10
        
        rev = rev * sign

        if rev > Max_Int or rev < Min_Int:
            return 0
        
        return rev