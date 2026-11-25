class Solution:
    def reorganizeString(self, s: str) -> str:
        res = ''
        maxHeap = []
        cnt = Counter(s)
        for key, val in cnt.items():
            heapq.heappush(maxHeap,[-val,key])
        pre = None
        while maxHeap or pre:
            if pre and not maxHeap: return ''
            cnt, c = heapq.heappop(maxHeap)
            cnt += 1
            res += c 
            if pre:
                heapq.heappush(maxHeap,pre)
                pre = None
            if cnt:
                pre = [cnt,c]
        return res 