import heapq
from typing import List


class Solution:

  def swimInWater(self, grid: List[List[int]]) -> int:
    n = len(grid)
    min_heap = [(grid[0][0], 0, 0)]  # (max_elevation, r, c)
    visited = set([(0, 0)])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while min_heap:
      max_elev, r, c = heapq.heappop(min_heap)

      if r == n - 1 and c == n - 1:
        return max_elev

      for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
          visited.add((nr, nc))
          next_elev = max(max_elev, grid[nr][nc])
          heapq.heappush(min_heap, (next_elev, nr, nc))

        