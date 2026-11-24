class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        map  = defaultdict(int)
        for n in nums:
            map[n] += 1
        
        temp = list(map.values())
        temp.sort()
        r = len(temp) - 1
        get = defaultdict(int)
        while k > 0:
            get[temp[r]] += 1
            r -= 1
            k -= 1
        for key, value in map.items():
            if value in get:
                res.append(key)
        return res

        