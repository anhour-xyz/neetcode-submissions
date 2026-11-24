class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p): return []
        map = defaultdict(int)
        for c in p:
            map[c] += 1
        res = []
        check = defaultdict(int)
        n = len(p)
        for i in range(n):
            if s[i] in map:
                check[s[i]] += 1
        if check == map: res.append(0)

        for i in range(1,len(s)-n+1):
            if s[i-1] in check:
                check[s[i-1]] -= 1
            if s[i+n-1] in map:
                check[s[i+n-1]] += 1
            if check == map: res.append(i)
        return res