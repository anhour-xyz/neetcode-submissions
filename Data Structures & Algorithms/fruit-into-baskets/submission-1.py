class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        map = defaultdict(int)
        l = 0
        res = 0
        for r in range(len(fruits)):
            map[fruits[r]] += 1
            while len(map) > 2:
                map[fruits[l]] -= 1
                if map[fruits[l]] == 0:
                    del map[fruits[l]]
                l += 1
            res = max(res, r-l+1)
        return res