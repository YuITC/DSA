# 74. Search a 2D Matrix
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # search row
        up, down = 0, len(matrix) - 1
        row = 0
        while up <= down:
            m = (up + down) // 2
            if matrix[m][0] <= target:
                row = m
                up = m + 1
            else:
                down = m - 1
            
        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            m = (l + r) // 2
            if matrix[row][m] == target:
                return True
            elif matrix[row][m] < target:
                l = m + 1
            else:
                r = m - 1
        return False
