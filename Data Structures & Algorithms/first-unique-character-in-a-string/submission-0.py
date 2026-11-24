class Solution:
    def firstUniqChar(self, s: str) -> int:
        map = defaultdict(int)
        for i in s:
            map[i] += 1
        for i in range(len(s)):
            if map[s[i]] == 1:
                return i
        return -1