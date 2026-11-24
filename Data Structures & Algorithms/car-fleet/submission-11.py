class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        map = {}
        for i, p in enumerate(position):
            map[p] = i

        position.sort()

        for i in range(len(position)-1,-1,-1):
            time = (target - position[i]) / speed[map[position[i]]]
            stack.append(time)
            while len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)