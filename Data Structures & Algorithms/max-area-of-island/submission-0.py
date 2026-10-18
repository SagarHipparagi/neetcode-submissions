class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        max_area = 0
        
        def dfs(r, c):
            # Check boundaries and if cell is water (0) or already visited (0)
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return 0
            
            # Mark the cell as visited by setting it to 0
            grid[r][c] = 0
            
            # Count current cell (1) + all 4-directional neighbors
            area = 1
            area += dfs(r + 1, c)
            area += dfs(r - 1, c)
            area += dfs(r, c + 1)
            area += dfs(r, c - 1)
            
            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r, c))
                    
        return max_area

        