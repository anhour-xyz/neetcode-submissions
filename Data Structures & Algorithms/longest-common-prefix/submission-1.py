class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        length = float('inf')
        target = ""
        for s in strs:
            if len(s) < length:
                length = len(s)
                target = s
        
        for word in strs:
            for i in range(len(target)):
                if word[i] != target[i]:
                    target = target[:i]
                    break
        return target
