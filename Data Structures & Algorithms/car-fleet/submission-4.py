class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        map = {}
        for i in range(len(position)):
            map[position[i]] = i

        position.sort()
        stack = []
        for i in range(len(position)-1,-1,-1):
            time = (target - position[i]) // speed[map[position[i]]]
            while stack and time <= stack[-1]:
                stack.pop()
            stack.append(time)
        return len(stack)
