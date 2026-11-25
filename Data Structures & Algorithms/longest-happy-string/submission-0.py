class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        maxHeap = []
        for cnt, char in [[-a,"a"], [-b,"b"],[-c,"c"]]:
            if cnt != 0:
                heapq.heappush(maxHeap,[cnt,char])
        heapq.heapify(maxHeap)
        res = ""
        while maxHeap:
            cnt, c = heapq.heappop(maxHeap)
            if len(res) > 1 and res[-1] == res[-2] == c:
                if not maxHeap:
                    break
                cnt1, c1 = heapq.heappop(maxHeap)
                res += c1
                cnt1 += 1
                if cnt1:
                    heapq.heappush(maxHeap,[cnt1,c1])
            else:
                res += c
                cnt += 1
            if cnt:
                heapq.heappush(maxHeap,[cnt,c])
        return res