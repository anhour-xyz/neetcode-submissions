class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        map = {
            "2":["a","b","c"],
            "3":["d","e","f"],
            "4":["g","h","i"],
            "5":["j","k","l"],
            "6":["m","n","o"],
            "7":["p","q","r","s"],
            "8":["t","u","v"],
            "9":["w","x","y","z"]
        }

        res = []
        def dfs(i,cur):
            if len(cur) == len(digits):
                res.append(''.join(cur.copy()))
                return
            if i >= len(digits): return
            for n in map[digits[i]]:
                cur.append(n)
                dfs(i+1,cur)
                cur.pop()
                dfs(i+1,cur)
        dfs(0,[])
        return res