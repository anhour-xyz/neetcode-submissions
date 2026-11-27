class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        map = defaultdict(int)
        for c in arr:
            map[c] += 1
        cnt = 0
        for c in arr:
            if map[c] == 1:
                cnt += 1
                if cnt == k: return c
        return ""