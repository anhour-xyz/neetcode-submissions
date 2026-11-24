class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = []
        i = 0
        stack = []
        while i < len(position):
            res.append([position[i], speed[i]])
            i += 1

        res.sort(key=lambda x: x[0], reverse=True)
        for i in range(len(res)):
            position = res[i][0]
            speed = res[i][1]
            time = (target - position) / speed
            stack.append(time)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)
