class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        map = defaultdict(int)
        for start, end in trust:
            map[end] += 1
            map[start] -= 1
        
        for key, val in map.items():
            if val == n - 1: return key
        return -1