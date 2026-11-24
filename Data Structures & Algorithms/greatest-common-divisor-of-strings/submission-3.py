class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        minLen = min(n,m)
        for i in range(minLen,0,-1):
            if n % i or m % i: continue
            target = str1[:i]
            check = True
            for j in range(0,n,i):
                if str1[j:j+i] != target:
                    check = False
                    break
            for j in range(0,m,i):
                if str2[j:j+i] != target:
                    check = False
                    break
            if check: return target
        return ""
