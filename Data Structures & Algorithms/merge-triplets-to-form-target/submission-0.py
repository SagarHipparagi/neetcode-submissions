from typing import List

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good_indices = set()
        
        for t in triplets:
            # Skip any triplet that has a value larger than target at any position
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
                
            # Record which target positions this valid triplet can match
            for i in range(3):
                if t[i] == target[i]:
                    good_indices.add(i)
                    
        # Return True if all three positions (0, 1, 2) can be matched
        return len(good_indices) == 3

        