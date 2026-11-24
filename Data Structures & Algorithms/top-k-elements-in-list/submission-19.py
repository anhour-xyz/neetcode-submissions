class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = defaultdict(int)
        for n in nums:
            map[n] += 1
        freq = defaultdict(list)
        for key, val in map.items():
            freq[val].append(key)
        res = []
        for i in range(len(nums),0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k: return res