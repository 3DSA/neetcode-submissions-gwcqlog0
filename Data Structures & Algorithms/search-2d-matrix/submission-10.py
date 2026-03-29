class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #binary seach on 2d array
        l = [0,0]
        r = [len(matrix)-1,len(matrix[0])-1]
        while l<=r:
            print(f"l: {l}.   r:{r}")
            middle = (l[0]*len(matrix[0]))+l[1]+1+ (r[0]*len(matrix[0]))+r[1]
            print(f"middle: {middle}")
            half = [(middle-1)//len(matrix[0]), (middle-1)%len(matrix[0])]
            print(f"half: {half}")
            print(matrix[half[0]][half[1]])
            if matrix[half[0]][half[1]] == target:
                return True
            elif matrix[half[0]][half[1]] < target:
                middle += 1
                l = [(middle-1)//len(matrix[0]), (middle-1)%len(matrix[0])]
            else:
                middle -= 1
                r = [(middle-1)//len(matrix[0]), (middle-1)%len(matrix[0])]
        return False

        