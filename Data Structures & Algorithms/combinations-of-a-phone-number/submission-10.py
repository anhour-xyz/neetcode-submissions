class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        map = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }
        res = []
        def dfs(i,cur):
            if len(cur) == len(digits):
                res.append(''.join(cur.copy()))
                return
            if i >= len(digits): return 
            for c in map[digits[i]]:
                cur.append(c)
                dfs(i+1,cur)
                cur.pop()
                dfs(i+1,cur)
        
        dfs(0,[])
        return res