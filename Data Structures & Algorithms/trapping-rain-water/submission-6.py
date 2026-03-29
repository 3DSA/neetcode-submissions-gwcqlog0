class Solution:
    def trap(self, height: List[int]) -> int:
        top = len(height) - 1 - height[::-1].index(max(height))
        
        # left of max
        l = 0
        total_water = 0
        while l < top:
            if height[l] == 0:
                l += 1
            else:
                r = l+1
                while height[l] > height[r]:
                    total_water += height[l] - height[r]
                    r +=1
                l = r

        # right of max
        l = len(height)-1
        while l > top:
            if height[l] == 0:
                l -= 1
            else:
                r = l-1
                while height[l] > height[r]:
                    total_water += height[l] - height[r]
                    r -=1
                l = r
        return total_water



        # right of right max v