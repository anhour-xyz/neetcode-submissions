class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        prefix = []
        cnt = 0
        for word in words:
            if word[0] in 'aeiou' and word[-1] in 'aeiou':
                cnt += 1
            prefix.append(cnt)
        res = []
        for start, end in queries:
            if start == 0:
                res.append(prefix[end])
            else:
                res.append(prefix[end]-prefix[start-1])
        return res