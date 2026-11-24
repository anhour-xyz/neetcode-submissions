class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        map = {}
        for i, c in enumerate(s):
            map[c] = i
        end = 0
        length = 0
        res = []
        for i, c in enumerate(s):
            end = max(end,map[c])
            length += 1
            if i == end:
                res.append(length)
                length = 0 
        return res