class Solution:
    def maxDifference(self, s: str) -> int:
        map = defaultdict(int)
        for i in s:
            map[i] += 1

        max_e = max_o = float('-inf')
        min_e = min_o = float('inf')
        for value in map.values():
            if value % 2 == 0:
                max_e = max(max_e,value)
                min_e = min(min_e,value)
            else:
                max_o = max(max_o,value)
                min_o = min(min_o,value)

        return max(abs(max_e-min_o), abs(max_o-min_e))
