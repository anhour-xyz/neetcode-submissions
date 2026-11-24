class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
    def addWord(self,word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.addWord(word)
        
        rows, cols = len(board), len(board[0])
        res = set()
        visit = set()

        def dfs(r,c,root,word):
            cur = root
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] not in cur.children or (r,c) in visit:
                return 
            word += board[r][c]
            cur = cur.children[board[r][c]]
            if cur.isWord: res.add(word)
            visit.add((r,c))
            dfs(r+1,c,cur,word)
            dfs(r-1,c,cur,word)
            dfs(r,c+1,cur,word)
            dfs(r,c-1,cur,word)
            visit.remove((r,c))

        for r in range(rows):
            for c in range(cols):
                dfs(r,c,root,'')
        return list(res)