from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        
        for num in nums:
            # Duplicate numbers cancel each other out (a ^ a = 0)
            result ^= num
            
        return result

        