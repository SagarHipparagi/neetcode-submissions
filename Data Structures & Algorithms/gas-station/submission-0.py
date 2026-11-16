from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # If total gas is less than total cost, no valid circuit exists
        if sum(gas) < sum(cost):
            return -1
            
        current_tank = 0
        start_index = 0
        
        for i in range(len(gas)):
            current_tank += gas[i] - cost[i]
            
            # If tank drops below 0, no station from start_index to i can be the start
            if current_tank < 0:
                start_index = i + 1
                current_tank = 0
                
        return start_index

        