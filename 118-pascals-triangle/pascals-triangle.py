class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        triangle = []

        for row_index in range(numRows):
            row = [1] * (row_index + 1)

            for col in range(1, row_index):
                row[col] = triangle[-1][col - 1] + triangle[-1][col]

            triangle.append(row)

        return triangle
