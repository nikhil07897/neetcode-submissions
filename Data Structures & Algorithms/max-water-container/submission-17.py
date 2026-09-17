class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        res = 0

        while l < r:
            area = min(height[l], height[r]) * (r - l)
            res = max(area, res)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res