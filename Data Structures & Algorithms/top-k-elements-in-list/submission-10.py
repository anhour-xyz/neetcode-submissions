class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        freq = defaultdict(list)

        for n in nums:
            count[n] += 1
        
        for key, val in count.items():
            freq[val].append(key)

        res = []
        for i in range(len(nums),0,-1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k: return res
        