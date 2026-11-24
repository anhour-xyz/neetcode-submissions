class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList.append(beginWord)
        map = defaultdict(list)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                map[pattern].append(word)

        q = deque()
        q.append(beginWord)
        res = 1
        visit = set()
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord: return res
                for j in range(len(word)):
                    pattern = word[:j]+ "*" + word[j+1:]
                    for neiword in map[pattern]:
                        if neiword not in visit:
                            visit.add(neiword)
                            q.append(neiword)
            res += 1
        return 0