class Solution:
    def maxDifference(self, s: str) -> int:
        map = defaultdict(int)
        for c in s:
            map[c] += 1
        odd_max = even_max = 0
        odd_min = even_min = float('inf')
        for key, val in map.items():
            if val % 2:
                odd_max = max(odd_max,val)
                odd_min = min(odd_min,val)
            else:
                even_min = min(even_min,val)
                even_max = max(even_max,val)
        return max(abs(odd_max - even_min), abs(odd_min - even_max))
        
        