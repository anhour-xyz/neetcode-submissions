class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t in "+-*/":
                second = stack.pop()
                first = stack.pop()
                if t == "+":
                    temp = first + second
                elif t == "-":
                    temp = first - second
                elif t == "*":
                    temp = first * second
                else:
                    temp = int(first/second)
                stack.append(temp)
            else:
                stack.append(int(t))
        return stack[0]