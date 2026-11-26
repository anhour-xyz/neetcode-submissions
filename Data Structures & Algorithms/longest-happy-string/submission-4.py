class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = ""
        maxHeap = []
        for cnt, c in [[-a,'a'],[-b,'b'],[-c,'c']]:
            if cnt != 0:
                heapq.heappush(maxHeap,[cnt,c])
        
        while maxHeap:
            cnt, c = heapq.heappop(maxHeap)
            if len(res) > 1 and res[-1] == res[-2] == c:
                if not maxHeap: break
                cnt2, c2 = heapq.heappop(maxHeap)
                cnt2 += 1
                res += c2
                if cnt2: heapq.heappush(maxHeap,[cnt2,c2])
            else:
                res += c
                cnt += 1
            if cnt: heapq.heappush(maxHeap,[cnt,c])
        return res