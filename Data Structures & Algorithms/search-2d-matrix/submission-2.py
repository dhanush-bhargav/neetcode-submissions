class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        left = 0
        right = m*n - 1

        while 0<=left<=right<m*n:
            mid = (left + right) // 2
            i = mid // n
            j = mid % n
            if i >= m or j >= n:
                return False
            if target == matrix[i][j]:
                return True
            elif target < matrix[i][j]:
                right = mid - 1
            elif target > matrix[i][j]:
                left = mid + 1
        return False