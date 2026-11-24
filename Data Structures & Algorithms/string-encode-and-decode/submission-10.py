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
        r = 0
        while r < len(s):
            temp = ""
            while s[r] != "~":
                temp += s[r]
                r += 1
            res.append(temp)
            r += 1
        return res