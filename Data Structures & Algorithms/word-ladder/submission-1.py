class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList.append(beginWord)
        check = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                check[pattern].append(word)
        res = 1
        visit = set([beginWord])
        q = deque()
        q.append(beginWord)
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord: return res
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for neiword in check[pattern]:
                        if neiword not in visit:
                            visit.add(neiword)
                            q.append(neiword)
            res += 1
        return 0