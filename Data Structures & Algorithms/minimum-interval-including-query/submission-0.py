import heapq
from typing import List

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # Sort intervals by their start time
        intervals.sort()
        
        min_heap = []  # Stores tuples of (interval_size, right_endpoint)
        res = {}
        i = 0
        n = len(intervals)
        
        # Process queries in ascending order while keeping original values for mapping
        for q in sorted(queries):
            # Add all intervals that start before or at the current query
            while i < n and intervals[i][0] <= q:
                left, right = intervals[i]
                heapq.heappush(min_heap, (right - left + 1, right))
                i += 1
            
            # Remove intervals that end before the current query
            while min_heap and min_heap[0][1] < q:
                heapq.heappop(min_heap)
            
            # The top of the heap holds the smallest valid interval
            res[q] = min_heap[0][0] if min_heap else -1
            
        # Map results back to the original query order
        return [res[q] for q in queries]

        