class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        map = defaultdict(int)
        for i in magazine:
            map[i] += 1
        for r in ransomNote:
            map[r] -= 1
        for value in map.values():
            if value < 0: return False
        return True