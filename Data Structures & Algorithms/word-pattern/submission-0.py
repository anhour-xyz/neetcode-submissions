class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(" ")
        if len(s) != len(pattern): return False
        map = {}
        visit = set()
        for i in range(len(pattern)):
            if pattern[i] in map:
                if s[i] != map[pattern[i]]:
                    return False
            else:
                if s[i] in visit: return False
                visit.add(s[i])
                map[pattern[i]] = s[i]
        return True