class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        map = defaultdict(int)
        for i in s1:
            map[i] += 1
        check = defaultdict(int)
        for i in range(len(s1)):
            if s2[i] in map:
                check[s2[i]] += 1
        if check == map: return True

        for i in range(1,len(s2)-len(s1)+1):
            if s2[i+len(s1)-1] in map:
                check[s2[i+len(s1)-1]] += 1
            if s2[i-1] in map:
                check[s2[i-1]] -= 1
            if check == map: return True
        return False