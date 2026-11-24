class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in s:
            if i != "]":
                stack.append(i)
            else:
                temp = ""
                while stack[-1] != "[":
                    temp = stack.pop() + temp
                stack.pop()
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append(temp * int(k))
        return ''.join(stack)