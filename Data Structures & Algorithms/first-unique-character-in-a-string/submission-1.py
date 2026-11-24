class Solution:
    def firstUniqChar(self, s: str) -> int:
        map = defaultdict(int)
        for i in s:
            map[i] += 1
        for i, c in enumerate(s):
            if map[c] == 1: return i
        return -1