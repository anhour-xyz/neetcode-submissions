class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        check1 = set()
        check2 = set()
        for n in nums1:
            check1.add(n)
        for n in nums2:
            check2.add(n)

        for n in check1:
            if n in check2:
                res.append(n)
        return res