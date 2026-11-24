class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map = {}
        check = set()
        for i in range(len(s)):
            if s[i] not in map:
                if t[i] in check:
                    return False
                else:
                    map[s[i]] = t[i]
                    check.add(t[i])
            else:
                if t[i] != map[s[i]]: return False
        return True
