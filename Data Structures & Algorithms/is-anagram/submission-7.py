class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map = defaultdict(int)
        for i in s:
            map[i] += 1
        for i in t:
            map[i] -= 1
        for val in map.values():
            if val != 0: return False
        return True