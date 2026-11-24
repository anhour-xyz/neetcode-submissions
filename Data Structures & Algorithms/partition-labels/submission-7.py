class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        map = {}
        for i in range(len(s)):
            map[s[i]] = i

        end = 0
        cnt = 0
        res = []
        for i,c in enumerate(s):
            end = max(end,map[c])
            cnt += 1
            if i == end:
                res.append(cnt)
                cnt = 0
        return res