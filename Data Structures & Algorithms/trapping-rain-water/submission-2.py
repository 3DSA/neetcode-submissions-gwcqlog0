class Solution:
    def last_occurence_max(self, arr):
        index = 0
        max_val = max(arr)
        for i in range(len(arr)-1, -1, -1):
            if arr[i] == max_val:
                index = i
                break
        return index
    def trap(self, height: List[int]) -> int:
        total_area = 0
        index_stop = self.last_occurence_max(height)
        ###### Everything left of the last occurence of the max value####
        i = 1
        j = 0
        switch = True
        area = 0
        while i <=index_stop and j <= index_stop:
            if switch:
                if height[i] >= height[j] and height[i] != 0:
                    switch = False
                    total_area += area
                    area = 0
                    j = i+1
                else:
                    area += height[j] - height[i]
                    i+=1
            else:
                if height[j] >= height[i] and height[j] != 0:
                    switch = True
                    total_area += area
                    area = 0
                    i = j+1
                else:
                    area += height[i] - height[j]
                    j+=1
        ######### End of the left side#################
        ###### Everything right of the last occurence of the max value####
        i = len(height)-2
        j = len(height)-1
        switch = True
        area = 0
        while i >=index_stop and j >= index_stop:
            if switch:
                if height[i] >= height[j] and height[i] != 0:
                    switch = False
                    print(area)
                    total_area += area
                    area = 0
                    j = i-1
                else:
                    area += height[j] - height[i]
                    i-=1
            else:
                if height[j] >= height[i] and height[j] != 0:
                    switch = True
                    print(area)
                    total_area += area
                    area = 0
                    i = j-1
                else:
                    area += height[i] - height[j]
                    j-=1
        ######### End of the left side#################
        return total_area
            

