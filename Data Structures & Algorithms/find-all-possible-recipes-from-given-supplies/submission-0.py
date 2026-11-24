class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        map = {}
        for i in range(len(recipes)):
            map[recipes[i]] = ingredients[i]
        res = []
        supplies = set(supplies)

        def dfs(food):
            if food in supplies: return True
            if food in visit: return False
            if food not in map: return False
            visit.add(food)
            for pre in map[food]:
                if not dfs(pre): return False
            supplies.add(food)
            return True

        for food in recipes:
            visit = set()
            if dfs(food): res.append(food)
        return res