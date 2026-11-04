class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total_sum = sum(nums)
        
        # If total sum is odd, it's impossible to partition into two equal integers
        if total_sum % 2 != 0:
            return False
            
        target = total_sum // 2
        
        # dp[i] will store True if a subset sum of 'i' is achievable
        dp = [False] * (target + 1)
        
        # Base case: A sum of 0 is always achievable
        dp[0] = True
        
        # Process each number in the input list
        for num in nums:
            # Loop backwards from target down to num
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]
                
        return dp[target]


        