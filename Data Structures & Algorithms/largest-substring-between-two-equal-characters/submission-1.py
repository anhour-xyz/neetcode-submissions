class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        map = defaultdict(list)
        for i in range(len(s)):
            map[s[i]].append(i)

        res = -1
        for value in map.values():
            if len(value) >= 2:
                res = max(res,value[-1]-value[0]-1)
        return res