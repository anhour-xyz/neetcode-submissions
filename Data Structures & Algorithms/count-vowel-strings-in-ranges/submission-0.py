class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        temp = []
        cnt = 0
        for word in words:
            for c in word:
                if c in 'aeiou':
                    cnt += 1
                    break
            temp.append(cnt)
        res = []
        for query in queries:
            start, end = query[0], query[1]
            if start == 0: res.append(temp[end])
            else: res.append(temp[end]-temp[start-1])
        return res
            