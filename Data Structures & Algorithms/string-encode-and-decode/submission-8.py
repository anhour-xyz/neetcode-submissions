class Solution:

    def encode(self, strs: List[str]) -> str:

        if not strs: return ""
        res = ""
        for s in strs:
            res += s
            res += "~"
        
        return res


    def decode(self, s: str) -> List[str]:
        if not s: return []
        res = []
        l = r = 0
        while r < len(s):
            while s[r] != "~":
                r += 1
            res.append(s[l:r])
            r += 1
            l = r
        return res
            
