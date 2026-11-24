class Solution:
    def findLucky(self, arr: List[int]) -> int:
        map = defaultdict(int)
        for a in arr:
            map[a] += 1
        res = -1
        for key, value in map.items():
            if key == value:
                res = max(res,key)
        return res 