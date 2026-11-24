class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        cnt = 0
        check = sorted(heights)
        for i in range(len(heights)):
            if heights[i] != check[i]: cnt += 1
        return cnt