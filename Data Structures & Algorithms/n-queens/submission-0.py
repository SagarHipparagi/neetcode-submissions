class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        # Sets to keep track of columns and diagonals under attack
        cols = set()
        pos_diag = set()  # (r + c)
        neg_diag = set()  # (r - c)
        
        res = []
        board = [["."] * n for _ in range(n)]
        
        def backtrack(r):
            # Base case: If we successfully filled all rows, add the solution
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            # Try placing a queen in each column of the current row
            for c in range(n):
                if c in cols or (r + c) in pos_diag or (r - c) in neg_diag:
                    continue
                
                # "Choose": Place the queen and mark its territory
                cols.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)
                board[r][c] = "Q"
                
                # "Explore": Move to the next row
                backtrack(r + 1)
                
                # "Unchoose": Remove the queen and unmark its territory (Backtrack)
                cols.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)
                board[r][c] = "."
                
        # Start backtracking from the 0-th row
        backtrack(0)
        return res

        