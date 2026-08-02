class Solution:
    def trap(self, height: List[int]) -> int:

        def findmax():
            curr = 0
            index = 0
            for i in range(len(height)):
                if height[i] >= curr:
                    curr = height[i]
                    index = i
            return index
        
        point = findmax()
        l = 0
        r = 0
        total = 0
        while r < point:
            if height[r] >= height[l]:
                l = r
            else:
                total += height[l]-height[r]
            r += 1
        
        l = len(height)-1
        r = l
        while r > point:
            if height[r] >= height[l]:
                l = r
            else:
                total += height[l]-height[r]
            r -= 1
        return total

        
        