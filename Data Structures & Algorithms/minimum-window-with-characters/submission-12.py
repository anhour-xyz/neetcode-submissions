class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): return ''
        map = defaultdict(int)
        meet = 0
        for i in t:
            map[i] += 1
        check = defaultdict(int)
        visit = set()
        l = 0
        res = ""
        length = float('inf')
        for r in range(len(s)):
            if s[r] in map:
                check[s[r]] += 1
                if check[s[r]] >= map[s[r]] and s[r] not in visit:
                    meet += 1
                    visit.add(s[r])
            while len(check) == len(map) and meet == len(map):
                if r - l + 1 < length:
                    length = r-l+1
                    res = s[l:r+1]
                if s[l] in check:
                    check[s[l]] -= 1
                    if check[s[l]] < map[s[l]]:
                        meet -= 1
                        visit.remove(s[l])
                l += 1

        return res