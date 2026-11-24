class Solution:
    def isValid(self, s: str) -> bool:
        map = {'(':')','[':']','{':"}"}
        stack = []
        for i in s:
            if i in map:
                stack.append(map[i])
            else:
                if not stack or i != stack.pop(): return False
        return len(stack) == 0