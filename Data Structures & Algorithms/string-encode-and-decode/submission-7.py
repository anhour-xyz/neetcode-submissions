class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs: return ''
        res = ""
        for s in strs:
            res += s
            res += "~"
        return res
    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []
        res = []
        i = j = 0
        while i < len(s):
            temp = ""
            while s[j] != "~":
                temp += s[j]
                j += 1
            res.append(temp)
            j += 1
            i = j
        return res
