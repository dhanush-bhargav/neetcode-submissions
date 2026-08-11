class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_sets = {}
        column_sets = {}
        square_sets = {}

        for row in range(0,9):
            if row not in row_sets.keys():
                row_sets[row] = set()
            for col in range(0,9):
                if col not in column_sets.keys():
                    column_sets[col] = set()
                current_square = (row // 3) * 3 + (col // 3)
                if current_square not in square_sets.keys():
                    square_sets[current_square] = set()
                
                if board[row][col] != ".":
                    if board[row][col] not in row_sets[row]:
                        row_sets[row].add(board[row][col])
                    else:
                        return False
                    if board[row][col] not in column_sets[col]:
                        column_sets[col].add(board[row][col])
                    else:
                        return False
                    if board[row][col] not in square_sets[current_square]:
                        square_sets[current_square].add(board[row][col])
                    else:
                        return False
        return True
