# 74. Search a 2D Matrix
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        
        # m*n matrix to array: M[x][y] -> A[x * n + y]
        # array to m*n matrix: a[x]    -> M[x / n][x % n]

        l, r = 0, n * m - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[mid // n][mid % n] < target:
                l = mid + 1
            elif matrix[mid // n][mid % n] > target:
                r = mid - 1
            else: 
                return True
        return False
