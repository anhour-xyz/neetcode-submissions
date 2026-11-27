class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1] * len(nums2)
        stack = []
        for i,n in enumerate(nums2):
            while stack and n > nums2[stack[-1]]:
                idx = stack.pop()
                res[idx] = n
            stack.append(i)
        map = {}
        for i in range(len(res)):
            map[nums2[i]] = res[i]
        ans = []
        for n in nums1:
            ans.append(map[n])
        return ans
