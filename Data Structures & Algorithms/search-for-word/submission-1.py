class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board), len(board[0])
        visited = set()
        def dfs(r,c,idx):
            if idx == len(word): return True
            if r < 0 or c < 0 or r >= row or c >= col or (r,c) in visited or board[r][c] != word[idx]:
                return False
            visited.add((r,c))
            found = (dfs(r+1,c,idx+1)or 
            dfs(r,c+1,idx+1) or 
            dfs(r-1,c,idx+1) or 
            dfs(r,c-1,idx+1))

            visited.remove((r,c))
            return found

        for r in range(row):
            for c in range(col):
                if board[r][c] == word[0] and dfs(r,c,0):
                    return True
        return False