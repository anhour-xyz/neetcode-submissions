class Solution:
    def minWindow(self, s: str, t: str) -> str:
        check = defaultdict(int)
        for i in t:
            check[i] += 1
        l = 0
        ans = ""
        res = float('inf')
        map = defaultdict(int)
        for r in range(len(s)):
            if s[r] in check:
                map[s[r]] += 1
            available = True
            while len(map) == len(check):
                for key, value in map.items():
                    if value < check[key]:
                        available = False
                if available == False: break
                if r-l+1 < res:
                    res = r-l+1
                    ans = s[l:r+1]
                if s[l] in map:
                    map[s[l]] -= 1
                    if map[s[l]] == 0:
                        del(map[s[l]])
                l += 1
        return ans       