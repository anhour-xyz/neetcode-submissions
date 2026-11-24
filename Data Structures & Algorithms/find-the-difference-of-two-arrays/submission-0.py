class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        res = []
        check1 = set()
        check2 = set()
        for n in nums1:
            check1.add(n)
        for n in nums2:
            check2.add(n)
        temp = []
        for n in set(nums1):
            if n not in check2:
                temp.append(n)
        res.append(temp)

        temp = []
        for n in set(nums2):
            if n not in check1:
                temp.append(n)
        res.append(temp)
        return res