class Solution:
    def maxDifference(self, s: str) -> int:
        map = defaultdict(int)
        for i in s:
            map[i] += 1

        max_o = float('-inf')
        min_e = float('inf')
        for value in map.values():
            if value % 2 == 0:
                min_e = min(min_e,value)
            else:
                max_o = max(max_o,value)


        return max_o - min_e
