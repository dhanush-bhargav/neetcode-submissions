class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        self.matrix[0][0] = matrix[0][0]
        for c in range(1, len(matrix[0])):
            self.matrix[0][c] = matrix[0][c] + self.matrix[0][c-1]
        
        for r in range(1, len(matrix)):
            self.matrix[r][0] = matrix[r][0] + self.matrix[r-1][0]

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                self.matrix[i][j] = matrix[i][j] + self.matrix[i][j-1] + self.matrix[i-1][j] - self.matrix[i-1][j-1]
    

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        result = self.matrix[row2][col2]
        if row1 > 0:
            result -= self.matrix[row1-1][col2]
        if col1 > 0:
            result -= self.matrix[row2][col1-1]
        if row1>0 and col1>0:
            result += self.matrix[row1-1][col1-1]
        return result


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)