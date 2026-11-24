class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        start = len(nums1) - n
        i = 0
        while start < len(nums1):
            nums1[start] = nums2[i]
            i += 1
            start += 1
        nums1.sort()

