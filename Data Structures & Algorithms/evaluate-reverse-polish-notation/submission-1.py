class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1: return int(tokens[0])
        num = []
        sym = []
        for t in tokens:
            if t == "+" or t == "-" or t == "/" or t == "*":
                sym.append(t)
            else:
                num.append(t)

        res = ""
        while num or sym:
            if num:
                res += num.pop()
            if sym:
                res += sym.pop()

        res = res[::-1]
        i = 3
        first = int(res[0])
        second = int(res[2])
        if res[1] == "+":
            temp = first + second
        elif res[1] == "-":
            temp = first - second
        elif res[1] == "/":
            temp = first // second
        else:
            temp = first * second
        while i < len(res):
            if res[i] == "+":
                temp = temp + int(res[i+1])
            elif res[i] == "-":
                temp = temp - int(res[i+1])
            elif res[i] == "/":
                temp = temp // int(res[i+1])
            else:
                temp = temp * int(res[i+1])
            i += 2
        return temp
            
            
