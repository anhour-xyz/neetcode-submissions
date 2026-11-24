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
            if stack and time <= stack[-1]:
                stack.pop()
            stack.append(time)
        
        return len(stack)
