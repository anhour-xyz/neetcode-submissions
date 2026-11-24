class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        map = defaultdict(int)
        res = 0
        n = len(s)
        l = 0
        for r in range(len(s)):
            map[s[r]] += 1
            while len(map) == 3:
                res += n - r
                map[s[l]] -= 1
                if map[s[l]] == 0: del map[s[l]]
                l += 1
        return res