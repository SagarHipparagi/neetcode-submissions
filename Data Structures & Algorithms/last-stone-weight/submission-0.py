import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Negate all elements to simulate a max-heap using Python's min-heap
        stones = [-s for s in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            # Pop the two largest stones (most negative values)
            y = -heapq.heappop(stones)
            x = -heapq.heappop(stones)
            
            # If they are not equal, push the difference back
            if y != x:
                heapq.heappush(stones, -(y - x))
                
        # Return the remaining stone weight, or 0 if none are left
        return -stones[0] if stones else 0

        