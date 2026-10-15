class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        
        rows, cols = len(board), len(board[0])
        
        def dfs(r, c):
            # Base case: Out of bounds or not an 'O'
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != "O":
                return
            
            # Temporarily mark the border-connected 'O' as 'T'
            board[r][c] = "T"
            
            # Explore all 4 adjacent directions
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
            
        # Step 1: Scan borders (first/last rows and columns)
        for r in range(rows):
            dfs(r, 0)            # Left border
            dfs(r, cols - 1)     # Right border
            
        for c in range(cols):
            dfs(0, c)            # Top border
            dfs(rows - 1, c)     # Bottom border
            
        # Step 2: Traverse the whole board to flip remaining 'O's and restore 'T's
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"  # Captured!
                elif board[r][c] == "T":
                    board[r][c] = "O"  # Restored to original safe state

        