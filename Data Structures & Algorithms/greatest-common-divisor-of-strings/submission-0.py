class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) < len(str2):
            target = str1
            minLen = len(str1)
        else:
            target = str1
            minLen = len(str1)

        for k in range(minLen,0,-1):
            target = target[:k]
            if len(str1) % k != 0 or len(str2) % k != 0: continue
            i = j = 0
            check = True
            while i < len(str1) and j < len(str2):
                if i < len(str1):
                    temp = str1[i:i+k]
                    if temp != target:
                        check = False
                        break
                    i += k
                if j < len(str2):
                    temp = str2[j:j+k]
                    if temp != target:
                        check = False
                        break
                    j += k
            if check: return target
        return ""