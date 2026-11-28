class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        map = defaultdict(int)
        for c in ransomNote:
            map[c] += 1
        for c in magazine:
            map[c] -= 1
        for val in map.values():
            if val > 0: return False
        return True