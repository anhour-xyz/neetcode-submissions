class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        n = len(skill)
        l, r = 0, len(skill) - 1
        res = 0
        target = skill[l] + skill[r]
        while l < r:
            if skill[l] + skill[r] != target: return -1
            res += skill[l] * skill[r]
            l += 1
            r -= 1
        return res
