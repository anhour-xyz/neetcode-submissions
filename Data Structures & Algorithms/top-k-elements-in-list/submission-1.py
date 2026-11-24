class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = defaultdict(int)
        for n in nums:
            map[n] += 1
        temp = []
        for value in map.values():
            temp.append(value)
        temp.sort()
        temp = temp[::-1]
        get = set()
        i = 0
        while i < len(temp) and k > 0:
            if temp[i] not in get:
                get.add(temp[i])
                k -= 1
            i += 1

        res = []
        for key, value in map.items():
            if value in get: res.append(key)
        return res