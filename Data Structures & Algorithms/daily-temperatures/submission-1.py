class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        for i in range(len(temperatures)-1):
            cnt = 1
            j = i + 1
            while j < len(temperatures) and temperatures[j] <= temperatures[i]:
                cnt += 1
                j += 1
            if j == len(temperatures) and temperatures[j-1] <= temperatures[i]:
                res.append(0)
            else:res.append(cnt)
        res.append(0)
        return res

