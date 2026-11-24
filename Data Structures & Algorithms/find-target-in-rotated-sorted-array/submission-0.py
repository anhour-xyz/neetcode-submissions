class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1 and nums[0] != target: return -1
        elif len(nums) == 1 and nums[0] == target: return 0
        l, r = 0, len(nums) - 1
        if nums[l] < nums[r]:
            while l <= r:
                mid = (l+r) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
        else:
            while l <= r:
                mid = (l+r) // 2
                if nums[mid] == target: return mid
                elif target < nums[mid] and target <= nums[r]:
                    l = mid + 1
                elif target < nums[mid] and target >= nums[l]:
                    r = mid - 1
                elif target > nums[mid] and target >= nums[r]:
                    l = mid + 1
                elif target > nums[mid] and target <= nums[r]:
                    r = mid - 1
        return -1