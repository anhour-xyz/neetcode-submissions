class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        map = defaultdict(int)
        for a in arr:
            map[a] += 1
        
        
        for a in arr:
            if map[a] == 1:
                if k != 1:
                    k -= 1
                else:
                    return a
        return ""
