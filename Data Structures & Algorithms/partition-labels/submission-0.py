from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # Record the last index at which each character appears
        last_index = {char: idx for idx, char in enumerate(s)}
        
        partitions = []
        start = 0
        end = 0
        
        for idx, char in enumerate(s):
            # Extend the current partition boundary to include the last occurrence of char
            end = max(end, last_index[char])
            
            # Once the current index reaches the boundary, close the partition
            if idx == end:
                partitions.append(end - start + 1)
                start = idx + 1
                
        return partitions

        