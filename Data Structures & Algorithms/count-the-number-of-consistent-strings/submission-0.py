class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        cnt = 0
        for word in words:
            check = True
            for i in word:
                if i not in allowed:
                    check = False
                    break
            if check == True: cnt += 1
        return cnt
