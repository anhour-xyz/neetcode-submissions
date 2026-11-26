class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        stack = []
        q = deque(senate)
        while q:
            if not stack:
                stack.append(q.popleft())
                continue
            c = q.popleft()
            if c != stack[-1]:
                q.append(stack.pop())
            else:
                stack.append(c)
        return "Radiant" if stack[0] == "R" else "Dire"