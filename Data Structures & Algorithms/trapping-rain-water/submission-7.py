class Solution:
    def trap(self, height: List[int]) -> int:
        def find():
            curr = 0
            index = 0
            for i in range(len(height)):
                if height[i] >= curr:
                    curr = height[i]
                    index = i
            return index

        top = find()
        l = 0
        water = 0
        for r in range(top):
            if height[l] == 0:
                l+= 1
            else:
                if height[r] >= height[l]:
                    l = r
                else:
                    water += height[l]-height[r]
        
        l = len(height)-1
        for r in range(len(height)-1, top, -1):
            if height[l] == 0:
                l-= 1
            else:
                if height[r] >= height[l]:
                    l = r
                else:
                    water += height[l]-height[r]
        return water
