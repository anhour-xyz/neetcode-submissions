class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        map = defaultdict(int)
        if k > len(s2): return False
        for i in s1:
            map[i] += 1
        check = defaultdict(int)
        for i in range(k):
            if s2[i] in map:
                check[s2[i]] += 1
        if check == map: return True

        for r in range(1,len(s2)-k+1):
            if s2[r+k-1] in map:
                check[s2[r+k-1]] += 1
            if s2[r-1] in map:
                check[s2[r-1]] -= 1
            if check == map: return True
        return False
        
        
