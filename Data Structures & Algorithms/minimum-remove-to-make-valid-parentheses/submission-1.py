class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        chars = list(s)
        stack = []
        for i,c in enumerate(s):
            if c == "(":
                stack.append(i)
            elif c == ")":
                if stack: stack.pop()
                else: chars[i] = ""

        while stack:
            chars[stack.pop()] = ""

        return ''.join(chars)