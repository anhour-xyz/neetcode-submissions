class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return ''
        map = defaultdict(int)
        meet = 0
        for c in t:
            map[c] += 1
        check = defaultdict(int)
        res = []
        visit = set()
        minLen = float('inf')
        l = 0
        for r in range(len(s)):
            if s[r] in map:
                check[s[r]] += 1
                if check[s[r]] >= map[s[r]] and s[r] not in visit:
                    meet += 1
                    visit.add(s[r])
            while len(map) == len(check) and meet == len(map):
                if r-l+1 < minLen:
                    minLen = r-l+1
                    res = [l,r+1]
                if s[l] in check:
                    check[s[l]] -= 1
                    if check[s[l]] < map[s[l]]:
                        meet -= 1
                        visit.remove(s[l])
                l += 1
        return s[res[0]:res[1]] if res != [] else '' 