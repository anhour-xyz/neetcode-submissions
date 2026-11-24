class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnt = Counter(tasks)
        maxHeap = []
        for value in cnt.values():
            heapq.heappush(maxHeap,-value)

        time = 0
        q = deque()
        while maxHeap or q:
            time += 1
            if maxHeap:
                cnt = heapq.heappop(maxHeap) + 1
                if cnt:
                    q.append([cnt,time + n])
                
            if q and time == q[0][1]:
                heapq.heappush(maxHeap,q.popleft()[0])
        return time