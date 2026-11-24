class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        invalid = set()
        stack = []
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            elif s[i] == ")":
                if stack:
                    stack.pop()
                else:
                    invalid.add(i)
        res = ""
        stack = set(stack)
        for i in range(len(s)):
            if i in invalid or i in stack: continue
            else:
                res += s[i]
        return res