class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max = 0
        left = 0
        right = len(heights)-1
        while left < right:
            if heights[left] < heights[right]:
                area = heights[left]* (right-left)
                if area > max:
                    max = area
                left +=1
            else: #left is greater than right
                area = heights[right]* (right-left)
                if area > max:
                    max = area
                right -=1
        return max