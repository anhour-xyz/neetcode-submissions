class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = sorted(zip(position,speed), reverse = True)
        res = 0
        preMax = 0
        for p, s in arr:
            time = (target-p) / s
            if time > preMax:
                preMax = time
                res += 1
        return res