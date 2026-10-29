from collections import defaultdict
from typing import List


class Solution:

  def findItinerary(self, tickets: List[List[str]]) -> List[str]:
    # Build adjacency list: sort destinations in reverse order
    # so we can pop the lexicographically smallest ones from the end
    graph = defaultdict(list)
    for src, dest in sorted(tickets, reverse=True):
      graph[src].append(dest)

    route = []

    def dfs(airport: str):
      while graph[airport]:
        next_dest = graph[airport].pop()
        dfs(next_dest)
      route.append(airport)

    dfs("JFK")
    return route[::-1]

        