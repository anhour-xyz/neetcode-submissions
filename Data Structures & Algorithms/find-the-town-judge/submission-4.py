class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        map = defaultdict(int)
        for start,end in trust:
            map[end] += 1
            map[start] -= 1
        
        for i in range(1,n+1):
            if map[i] == n - 1: return i 
        return -1