class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        map = {}
        visit = set()
        for i in range(len(s)):
            if s[i] in map:
                if t[i] != map[s[i]]: return False
            else:
                if t[i] in visit: return False
                visit.add(t[i])
                map[s[i]] = t[i]
        return True