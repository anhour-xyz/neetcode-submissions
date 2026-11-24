class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minLen = float('inf')
        for s in strs:
            if len(s) < minLen:
                minLen = len(s)
                target = s
        
        for s in strs:
            for i in range(len(target)):
                if target[i] != s[i]:
                    target = target[:i]
                    break
                    
        return target