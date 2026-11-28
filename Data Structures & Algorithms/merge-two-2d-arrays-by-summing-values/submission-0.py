class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        map = defaultdict(int)
        for i, n in nums1:
            map[i] += n
        for j, n in nums2:
            map[j] += n
        res = []
        for key, val in map.items():
            res.append([key,val])
        res.sort(key=lambda x:x[0])
        return res