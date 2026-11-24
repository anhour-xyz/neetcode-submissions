class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        self.res = float('inf')

        def dfs(i,cur,total):
            if total == amount:
                self.res = min(self.res,len(cur))
                return
            if total > amount or i >= len(coins): return
            cur.append(coins[i])
            dfs(i,cur,total + coins[i])
            cur.pop()
            dfs(i+1,cur,total)
        dfs(0,[],0)
        return self.res if self.res != float('inf') else -1