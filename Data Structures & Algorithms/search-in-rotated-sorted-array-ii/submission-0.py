class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l,r = 0, len(nums) - 1
        while l <= r:
            mid = (l+r) // 2
            if target == nums[mid]: return True
            if nums[l] > nums[r]:
                if target < nums[mid] and target <= nums[r]: l = mid + 1
                else:
                    r = mid - 1
            elif nums[l] < nums[r]:
                if target < nums[mid]:r = mid - 1
                else: l = mid + 1
            else:
                if nums[l+1] == nums[r-1]:
                    return False
                else:
                    if target < nums[mid]: l = mid + 1
                    else: r = mid - 1
        return False