class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        arr = list(s)
        stack = []
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif c == ')':
                if not stack:
                    arr[i] = ''
                else:
                    stack.pop()
        while stack:
            arr[stack.pop()] = ''
        return ''.join(arr)