class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        l = r = 0
        while l < len(s) and r < len(s):
            check = set()
            while s[r] in set(s[r+1:]) or len(check) > 0:
                r += 1
                check.add(s[r])
                if s[r] not in set(s[r+1:]):
                    check.remove(s[r]) 
            res.append(r-l+1)
            r += 1
            l = r
        return res
        
        