from typing import List
from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # 1. Build an adjacency list representation of the directed graph
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
            
        # 2. Min-heap keeps track of (accumulated_time, current_node)
        # It ensures we always process the node reachable with the shortest time next
        min_heap = [(0, k)]
        
        # 3. Dictionary to track the absolute shortest time to reach each node
        visited = {}
        
        while min_heap:
            time, node = heapq.heappop(min_heap)
            
            # If the node has already been visited with a shorter path, skip it
            if node in visited:
                continue
                
            # Record the shortest time to this node
            visited[node] = time
            
            # Traverse neighbors
            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (time + weight, neighbor))
                    
        # 4. If all n nodes are visited, return the maximum time taken.
        # Otherwise, return -1 (network is disconnected / unreachable).
        return max(visited.values()) if len(visited) == n else -1

        