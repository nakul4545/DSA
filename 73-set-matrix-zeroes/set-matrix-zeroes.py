class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        row_zero = set()
        col_zero = set()
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    row_zero.add(row)
                    col_zero.add(col)
        for row in range(rows):
            for col in range(cols):
                if row in row_zero or col in col_zero:
                    matrix[row][col] = 0