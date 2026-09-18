import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        
        while l <= r:
            k = (l + r) // 2
            
            # Calculate total hours needed for speed k
            total_hours = sum(math.ceil(pile / k) for pile in piles)
            
            if total_hours <= h:
                res = k  # Try a slower speed
                r = k - 1
            else:
                l = k + 1  # Need a faster speed
                
        return res

        