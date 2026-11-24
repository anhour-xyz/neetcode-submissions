class Solution:
    def minWindow(self, s: str, t: str) -> str:
        check = defaultdict(int)
        for i in t:
            check[i] += 1
        l = 0
        ans = ""
        res = float('inf')
        map = defaultdict(int)
        visit = set()
        meet = 0
        for r in range(len(s)):
            if s[r] in check:
                map[s[r]] += 1
                if map[s[r]] >= check[s[r]] and s[r] not in visit: 
                    meet += 1
                    visit.add(s[r])
            available = True
            while len(map) == len(check) and meet == len(check):
                if r-l+1 < res:
                    res = r-l+1
                    ans = s[l:r+1]
                if s[l] in map:
                    map[s[l]] -= 1
                    if map[s[l]] < check[s[l]]: 
                        meet -= 1
                        visit.remove(s[l])

                l += 1
        return ans       