class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position = sorted(zip(position,speed), reverse = True)
        preTime = -1
        res = 0
        for i, p in position:
            time = (target - i) / p
            if time > preTime:
                preTime = time
                res += 1
        return res