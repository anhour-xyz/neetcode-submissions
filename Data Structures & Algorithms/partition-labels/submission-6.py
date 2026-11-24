class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        map = {}
        for i in range(len(s)):
            map[s[i]] = i
        res = []
        end = 0
        length = 0
        for i in range(len(s)):
            end = max(end,map[s[i]])
            length += 1
            if i == end:
                res.append(length)
                length = 0
        return res