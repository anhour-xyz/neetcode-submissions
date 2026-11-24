class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        h,w = len(matrix), len(matrix[0])
        l,r = 0, h*w-1
        while l <= r:
            mid = (l+r)//2
            num = matrix[mid//w][mid%w]
            if num == target:
                return True
            elif num < target:
                l = mid + 1
            else:
                r = mid - 1
        return False