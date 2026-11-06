from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total_sum = sum(nums)
        
        # Mathematical edge cases: 
        # 1. target is out of the achievable range [-total_sum, total_sum]
        # 2. (total_sum - target) must be even because moving an element from 
        #    positive to negative changes the overall sum by a multiple of 2.
        if abs(target) > total_sum or (total_sum - target) % 2 != 0:
            return 0
            
        # The problem reduces to finding a subset that sums up to:
        # subset_target = (total_sum - target) // 2
        subset_target = (total_sum - target) // 2
        
        # DP array initialized to 0s, with 1 way to make a sum of 0 (empty subset)
        dp = [0] * (subset_target + 1)
        dp[0] = 1
        
        # Update the DP array backwards to avoid using the same element twice
        for num in nums:
            for j in range(subset_target, num - 1, -1):
                dp[j] += dp[j - num]
                
        return dp[subset_target]

# Example usage:
if __name__ == "__main__":
    sol = Solution()
    print(sol.findTargetSumWays([1, 1, 1, 1, 1], 3))  # Output: 5
    print(sol.findTargetSumWays([1], 1))              # Output: 1

        