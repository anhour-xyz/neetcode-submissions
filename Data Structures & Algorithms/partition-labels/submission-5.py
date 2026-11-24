class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        map = {}
        for i in range(len(s)):
            map[s[i]] = i
        end = 0
        count = 0
        for i in range(len(s)):
            end = max(map[s[i]],end)
            count += 1
            if i == end:
                res.append(count)
                count = 0
        return res