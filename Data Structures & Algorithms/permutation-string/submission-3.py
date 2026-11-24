class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        map1 = defaultdict(int)
        for s in s1:
            map1[s] += 1

        for l in range(len(s2)):
            temp = map1.copy()
            if s2[l] in temp:
                temp[s2[l]] -= 1
                r = l + 1
                while r < len(s2) and s2[r] in temp:
                    if temp[s2[r]] == 0: break
                    temp[s2[r]] -= 1
                    r += 1
                r -= 1
                if r-l + 1 == len(s1):
                    return True
        return False



