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
            while i < len(str1) or j < len(str2):
                if i < len(str1):
                    temp1 = str1[i:i+k]
                    if temp1 != target:
                        check = False
                        break
                    i += k
                if j < len(str2):
                    temp2 = str2[j:j+k]
                    if temp2 != target:
                        check = False
                        break
                    j += k
            if check: return target
        return ""