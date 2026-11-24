class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        check = set()
        for n in nums1:
            check.add(n)
        res = []
        for n in nums2:
            if n in check:
                res.append(n)
                check.remove(n)
        return res