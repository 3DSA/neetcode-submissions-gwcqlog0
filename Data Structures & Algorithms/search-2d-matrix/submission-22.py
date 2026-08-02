class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = (len(matrix) * len(matrix[0])) - 1
        while l <=r:
            half = (l+r) // 2
            i = half // len(matrix[0])
            j = half % len(matrix[0])
            print(l)
            print(r)
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                l = half + 1
            else:
                r = half-1
        return False

        