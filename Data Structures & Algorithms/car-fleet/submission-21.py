class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = sorted(zip(position, speed), reverse = True)
        res = 0
        preTime = 0
        for p, s in arr:
            time = (target-p) / s
            if time > preTime:
                preTime = time
                res += 1
        return res