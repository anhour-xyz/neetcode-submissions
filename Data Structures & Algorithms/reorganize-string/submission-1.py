class Solution:
    def reorganizeString(self, s: str) -> str:
        res = ''
        cnt = Counter(s)
        maxHeap = []
        for key, val in cnt.items():
            heapq.heappush(maxHeap,[-val,key])

        q = deque()

        while maxHeap or q:
            if maxHeap:
                cnt, c = heapq.heappop(maxHeap)
                res += c
                cnt += 1
                if cnt:
                    q.append([cnt,c])
            if not maxHeap and q:
                heapq.heappush(maxHeap,q.popleft())

        return res