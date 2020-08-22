def area(heights, i, j):
    height = min(heights[i], heights[j])
    width = abs(i - j)
    return height * width

class Solution:
    def maxArea(self, heights) -> int:
        i = 0
        j = len(heights) - 1
        maxArea = area(heights, i, j)
        while i < j:
            if heights[i] > heights[j]:
                j -= 1
            else:
                i += 1
            maxArea = max(maxArea, area(heights, i, j))
        return maxArea