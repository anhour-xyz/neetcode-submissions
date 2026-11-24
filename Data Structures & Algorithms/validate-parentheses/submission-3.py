class Solution:
    def isValid(self, s: str) -> bool:
        map = {'[':']', '(':')', '{':'}'}
        stack = []
        for i in s:
            if i in map:
                stack.append(map[i])
            else:
                if i != stack.pop() or not stack: return False
        return len(stack) == 0
