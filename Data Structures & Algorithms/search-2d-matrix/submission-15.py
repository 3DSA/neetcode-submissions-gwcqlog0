class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # use it like a multiplication table
        l = 0
        r = len(matrix) * len(matrix[0])-1
        while l <= r:
            point = (l+r) // 2
            index = [point // len(matrix[0]), point % len(matrix[0])]
            if matrix[index[0]][index[1]] == target:
                return True

            elif matrix[index[0]][index[1]] < target:
                l = point + 1
            else:
                r = point - 1


        return False