class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_ = 0
        n = len(heights)
        l, r = 0, n - 1

        while l < r:
            area = min(heights[l], heights[r]) * (r- l)
            max_ = max(area, max_)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1

        return max_
        