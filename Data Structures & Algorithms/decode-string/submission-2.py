class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            if c != ']':
                stack.append(c)
            else:
                word = ''
                while stack[-1] != '[':
                    word = stack.pop() + word
                stack.pop()
                num = ''
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                stack.append(word * int(num))
        return ''.join(stack)