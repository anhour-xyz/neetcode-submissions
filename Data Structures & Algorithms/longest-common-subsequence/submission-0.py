class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l_text1 = len(text1)
        l_text2 = len(text2)
        res = 0
        if l_text1 <= l_text2:
            i = j = 0
            cnt = 0
            while j < l_text2:
                if i < len(text1) and text2[j] == text1[i]:
                    cnt += 1
                    i += 1
                j += 1
        else:
            i = j = 0
            cnt = 0
            while j < l_text1:
                if i < len(text2) and text1[j] == text2[i]:
                    cnt += 1
                    i += 1
                j += 1

        return cnt
                    