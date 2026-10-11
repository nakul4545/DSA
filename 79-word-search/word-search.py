class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        # x = [-1,1,0,0]
        # y = [0,0,-1,1]
        rows = len(board)
        cols = len(board[0])
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        def dfs(row,col, index):
            if board[row][col] != word[index]:
                return False
            if index == len(word) -1:
                return True
            original = board[row][col]
            board[row][col] = "#"
            for dr, dc in directions:
                nr , nc = row + dr, col + dc
                if (0<= nr< rows and 0 <= nc < cols and board[nr][nc] != "#" and dfs(nr,nc, index+1)):
                    board[row][col] = original
                    return True
            board[row][col] = original
            return False
        for row in range(rows):
            for col in range(cols):
                if dfs(row, col, 0):
                    return True
        return False
        

