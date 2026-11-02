from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Iterate backwards from the third-to-last step down to 0
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])
        
        # The answer is the minimum cost starting from step 0 or step 1
        return min(cost[0], cost[1])

        