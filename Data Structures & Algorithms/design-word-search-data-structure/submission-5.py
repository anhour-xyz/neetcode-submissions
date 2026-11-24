class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for w in word:
            if w not in cur.children:
                cur.children[w] = TrieNode()
            cur = cur.children[w]
        cur.isWord = True

    def search(self, word: str) -> bool:
        
        def dfs(i,root):
            cur = root
            for j in range(i,len(word)):
                c = word[j]
                if c == ".":
                    for child in cur.children.values():
                        if dfs(j+1,child): return True
                    return False
                else:
                    if c not in cur.children: return False
                    cur = cur.children[c]
            return cur.isWord

        return dfs(0,self.root)