class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        q = deque()
        for i, n in enumerate(tickets):
            q.append([i,n])
        time = 0
        while q:
            time += 1
            idx, n = q.popleft()
            n -= 1
            if n == 0 and idx == k: return time
            if n != 0:
                q.append([idx,n])

