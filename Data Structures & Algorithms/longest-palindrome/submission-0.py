class Solution:
    def longestPalindrome(self, s: str) -> int:
        cnt = defaultdict(int)
        for c in s:
            cnt[c] += 1
        maxOdd = 0
        res = 0
        for key,val in cnt.items():
            if val % 2 == 0:
                res += val
            else:
                if val > maxOdd:
                    maxOdd = val
                    check = key
        for key, val in cnt.items():
            if val % 2 and key != check:
                res += val - 1

        return res + maxOdd
