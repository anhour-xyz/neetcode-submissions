class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        map = defaultdict(int)
        for c in text:
            if c in 'balon':
                map[c] += 1
        if len(map) != 5: return 0
        res = float('inf')
        for key, val in map.items():
            if key == "l" or key == 'o':
                res = min(res, val // 2)
            else:
                res = min(res, val)
        return res