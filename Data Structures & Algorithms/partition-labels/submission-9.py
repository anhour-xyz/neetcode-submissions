class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        map = {}
        for i, c in enumerate(s):
            map[c] = i

        res = []
        end = 0
        cnt = 0
        for i, c in enumerate(s):
            end = max(end,map[c])
            cnt += 1
            if i == end:
                res.append(cnt)
                cnt = 0
        return res