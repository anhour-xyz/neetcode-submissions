class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): return ''
        map = defaultdict(int)
        for c in t:
            map[c] += 1
        check = defaultdict(int)
        l = 0
        visited = set()
        minLen = float('inf')
        res = []
        meet = 0
        for r in range(len(s)):
            if s[r] in map:
                check[s[r]] += 1
                if check[s[r]] >= map[s[r]] and s[r] not in visited:
                    meet += 1
                    visited.add(s[r])

            while len(check) == len(map) and meet == len(map):
                if r - l + 1 < minLen:
                    minLen = r - l + 1
                    res = [l,r+1]
                if s[l] in check:
                    check[s[l]] -= 1
                    if check[s[l]] < map[s[l]]:
                        meet -= 1
                        visited.remove(s[l])
                l += 1

        return s[res[0]:res[1]] if minLen != float('inf') else ""