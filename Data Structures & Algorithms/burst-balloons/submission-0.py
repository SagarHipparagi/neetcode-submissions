class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # Prepend and append 1 to handle boundary conditions
        balloons = [1] + nums + [1]
        n = len(balloons)
        
        # dp[i][j] represents the maximum coins obtained by bursting balloons in the range (i, j) exclusive
        dp = [[0] * n for _ in range(n)]
        
        # Length of the sub-array
        for length in range(2, n):
            for left in range(0, n - length):
                right = left + length
                # Try every balloon 'i' as the last balloon to be burst in the range (left, right)
                for i in range(left + 1, right):
                    coins = balloons[left] * balloons[i] * balloons[right]
                    coins += dp[left][i] + dp[i][right]
                    dp[left][right] = max(dp[left][right], coins)
                    
        return dp[0][n - 1]

        