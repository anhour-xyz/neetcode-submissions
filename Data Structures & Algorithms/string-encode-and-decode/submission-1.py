class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs: return ""
        temp = ""
        for s in strs:
            temp += s
            temp += "#"
        return temp


    def decode(self, s: str) -> List[str]:
        if not s: return []
        strs = []
        i = 0
        while i < len(s):
            temp = ""
            while s[i] != "#":
                temp += s[i]
                i += 1
            strs.append(temp)
            i += 1
        return strs
