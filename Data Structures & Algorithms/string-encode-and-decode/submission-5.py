class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs: return ''
        temp = ""
        for s in strs:
            temp += s
            temp += '_'
        return temp

    def decode(self, s: str) -> List[str]:
        if not s: return []
        res = []
        i = 0
        while i < len(s):
            temp = ""
            while s[i] != '_':
                temp += s[i]
                i += 1
            res.append(temp)
            i += 1
        return res
