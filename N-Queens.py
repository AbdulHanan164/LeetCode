class Solution:
    def solveNQueens(self, n):
        def is_valid(row, col):
            # Check if no queens attack in the current position
            for r in range(row):
                if board[r][col] == 'Q':
                    return False
                if col - (row - r) >= 0 and board[r][col - (row - r)] == 'Q':
                    return False
                if col + (row - r) < n and board[r][col + (row - r)] == 'Q':
                    return False
            return True
        
        def place_queen(row):
            if row == n:
                result.append(["".join(board[i]) for i in range(n)])
                return
            for col in range(n):
                if is_valid(row, col):
                    board[row][col] = 'Q'
                    place_queen(row + 1)
                    board[row][col] = '.'
        
        board = [['.'] * n for _ in range(n)]
        result = []
        place_queen(0)
        return result
