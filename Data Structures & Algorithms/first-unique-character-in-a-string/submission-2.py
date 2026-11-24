class Solution:
    def firstUniqChar(self, s: str) -> int:
        map = defaultdict(int)
        for n in s:
            map[n] += 1
        for i in range(len(s)):
            if map[s[i]] == 1: return i
        return -1