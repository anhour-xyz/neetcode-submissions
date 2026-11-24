class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        map = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                map[pattern].append(word)

        q = deque()
        q.append(beginWord)
        cnt = 1
        visit = set()
        visit.add(beginWord)

        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord: return cnt
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for nei in map[pattern]:
                        if nei not in visit:
                            q.append(nei)
                            visit.add(nei)
            cnt += 1
        return 0