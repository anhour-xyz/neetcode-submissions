class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        map1 = defaultdict(int)
        for s in s1:
            map1[s] += 1

        for l in range(len(s2)):
            temp = map1
            if s2[l] in temp:
                temp[s2[l]] -= 1
                r = l + 1
                while r < len(s2) and s2[r] in temp:
                    temp[s2[r]] -= 1
                    if temp[s2[r]] < 0: break
                    r += 1
                r -= 1
                if r-l + 1 == len(s1) and all(value == 0 for value in temp.values()):
                    return True
        return False



