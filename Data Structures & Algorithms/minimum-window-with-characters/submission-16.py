class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): return ''
        map = defaultdict(int)
        for i in t:
            map[i] += 1

        l = 0
        meet = 0
        res = ""
        length = float('inf')
        check = defaultdict(int)
        visit = set()
        for r in range(len(s)):
            if s[r] in map:
                map[s[r]] += 1
                if map[s[r]] >= check[s[r]] and s[r] not in visit:
                    visit.add(s[r])
                    meet += 1
            while len(map) == len(check) and meet == len(map):
                if r-l+1 < length:
                    length = r-l+1
                    res = s[l:r+1]
                if s[l] in map:
                    check[s[l]] -= 1
                    if check[s[l]] < map[s[l]]:
                        meet -= 1
                        visit.remove(s[l])

                l += 1
        return res
