class Solution:
    def trap(self, height: List[int]) -> int:
        occurence = len(height) - 1 - height[::-1].index(max(height))
        i = 0
        j = 1
        area = 0
        # left of highest occurence
        while i <= occurence and j <= occurence:
            print(f"i:{i}  j:{j}   area: {area}")
            if height[i] > height[j]:
                if i < j:
                    area += height[i]-height[j]
                    j +=1
                else:
                    j = i+1
            else: # j >= i
                if j < i:
                    area += height[j]-height[i]
                    i+=1
                else:
                    i=j+1
        # right of occurence
        i = len(height)-1
        j = len(height)-2
        while i >= occurence and j >= occurence:
            if height[i] > height[j]:
                if i > j:
                    area += height[i]-height[j]
                    j -=1
                else:
                    j = i-1
            else: # j >= i
                if j > i:
                    area += height[j]-height[i]
                    i-=1
                else:
                    i=j-1
        return area

        


        