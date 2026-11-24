class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        map = defaultdict(int)
        check = defaultdict(int)
        n = len(s1)
        for i in range(n):
            map[s1[i]] += 1
        for i in range(n):
            if s2[i] in map:
                check[s2[i]] += 1
        if check == map: return True

        for i in range(1,len(s2)-n+1):
            if s2[i-1] in map:
                check[s2[i-1]] -= 1
            if s2[i+n-1] in map:
                check[s2[i+n-1]] += 1
            if check == map: return True
        return False

