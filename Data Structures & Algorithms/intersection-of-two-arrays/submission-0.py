class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        check = set()
        for n in nums1:
            check.add(n)
        nums2 = set(nums2)
        res = []
        for n in nums2:
            if n in check:
                res.append(n)
        return res