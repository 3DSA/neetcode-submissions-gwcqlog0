class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        area = 0
        while left < right:
            if heights[left] > heights[right]:
                if (heights[right]*(right-left)) > area:
                    area = heights[right]*(right-left)
                right -=1
            else:
                if (heights[left]*(right-left)) > area:
                    area = heights[left]*(right-left)
                left +=1
        return area
