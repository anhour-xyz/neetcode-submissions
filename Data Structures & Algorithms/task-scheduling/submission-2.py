class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnt = list(Counter(tasks).values())
        max_cnt = max(cnt)
        cnt_max = cnt.count(max_cnt)

        return max(len(tasks),(max_cnt-1) * (n+1) + cnt_max)
