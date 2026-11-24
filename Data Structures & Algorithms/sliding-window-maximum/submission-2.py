class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        localmax = float('-inf')
        i = 0
        index = len(nums) - 1
        while i <= len(nums) - k:
            n = i
            if index >= i and index < i + k - 1:
                if nums[i+k-1] >= localmax:
                    res.append(nums[i+k-1])
                    localmax = nums[i+k-1]
                    index = nums.index(localmax)
                else:
                    res.append(localmax)

            else:
                localmax = nums[i]
                for j in range(k):
                    localmax = max(localmax, nums[n])
                    index = nums.index(localmax)
                    n += 1
                res.append(localmax)
            i += 1
        return res
            