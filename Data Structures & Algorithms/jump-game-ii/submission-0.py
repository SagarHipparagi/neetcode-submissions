from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        current_end = 0
        farthest = 0
        
        # Stop at len(nums) - 1 because you don't need to jump once you reach the last index
        for i in range(len(nums) - 1):
            # Update the farthest index reachable from the current window
            farthest = max(farthest, i + nums[i])
            
            # If you reach the end of the current jump's range, commit to a new jump
            if i == current_end:
                jumps += 1
                current_end = farthest
                
                # Optional early exit if the last index is already within reach
                if current_end >= len(nums) - 1:
                    break
                    
        return jumps
