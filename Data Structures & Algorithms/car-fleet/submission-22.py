class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = sorted(zip(position,speed),reverse = True)
        res = 0
        preEnd = -1
        for p, s in arr:
            t = (target-p) / s
            if t > preEnd:
                preEnd = t
                res += 1
        return res
