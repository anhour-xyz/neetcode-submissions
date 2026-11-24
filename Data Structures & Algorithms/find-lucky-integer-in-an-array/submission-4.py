class Solution:
    def findLucky(self, arr: List[int]) -> int:
        map = defaultdict(int)
        for a in arr:
            map[a] += 1
        res = -1
        for key,val in map.items():
            if key == val: res = max(res,key)
        return res
        
        