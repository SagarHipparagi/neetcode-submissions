from functools import cache
from typing import List


class Solution:

  def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
    if not matrix or not matrix[0]:
      return 0

    rows, cols = len(matrix), len(matrix[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    @cache
    def dfs(r: int, c: int) -> int:
      best = 1  # Every cell itself is a path of length 1
      for dr, dc in directions:
        nr, nc = r + dr, c + dc
        # Move only within bounds and to strictly greater values
        if (
            0 <= nr < rows
            and 0 <= nc < cols
            and matrix[nr][nc] > matrix[r][c]
        ):
          best = max(best, 1 + dfs(nr, nc))
      return best

    # Compute the longest path starting from every cell and return the overall maximum
    return max(dfs(r, c) for r in range(rows) for c in range(cols))


# Example usage:
if __name__ == "__main__":
  sol = Solution()
  grid = [[9, 9, 4], [6, 6, 8], [2, 1, 1]]
  print(sol.longestIncreasingPath(grid))  # Output: 4 (Path: 1 -> 2 -> 6 -> 9)

        