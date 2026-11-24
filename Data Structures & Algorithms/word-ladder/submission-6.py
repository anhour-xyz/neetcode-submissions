class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        map = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i+1:]
                map[pattern].append(word)
        
        q = deque()
        q.append(beginWord)
        step = 0
        visit = set()
        visit.add(beginWord)
        while q:
            step += 1
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord: return step
                for i in range(len(word)):
                    pattern = word[:i] + '*' + word[i+1:]
                    for nei in map[pattern]:
                        if nei not in visit:
                            q.append(nei)
                            visit.add(nei)
        return 0

        