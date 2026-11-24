class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        ans = [0] * (len(nums)-k+1)
        for i, n in enumerate(nums):
            while q and n >= nums[q[-1]]:
                q.pop()
            q.append(i)
            left = i - k + 1
            if q[0] < left: q.popleft()
            if left >= 0: ans[left] = nums[q[0]]
        return ans