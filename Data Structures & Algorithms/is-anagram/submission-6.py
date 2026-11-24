class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map = defaultdict(int)
        for i in s:
            map[i] += 1
        for i in t:
            map[i] -= 1
        for value in map.values():
            if value != 0: return False
        return True