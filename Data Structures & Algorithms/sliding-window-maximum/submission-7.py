class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        maximum = defaultdict(int)
        for i in range(k):
            maximum[nums[i]] +=1          
        res.append(max(maximum.keys()))

        for i in range(1,len(nums)-k+1):
            maximum[nums[i-1]] -= 1
            if maximum[nums[i-1]] == 0:
                del maximum[nums[i-1]]
            new_num = nums[i+k-1]
            maximum[new_num] += 1
            if new_num > max(maximum.keys()):
                res.append(new_num)
            else:
                res.append(max(maximum.keys()))

        return res