class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        map = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                map[pattern].append(word)

        res = 1
        visit = set([beginWord])
        q = collections.deque()
        q.append(beginWord)
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord: return res
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for neiword in map[pattern]:
                        if neiword not in visit:
                            visit.add(neiword)
                            q.append(neiword)
            res += 1
        return 0