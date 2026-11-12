class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        if m < n:
            return 0

        # dp[j] stores the number of ways to form t[:j]
        dp = [0] * (n + 1)
        dp[0] = 1  # An empty target string can always be formed in 1 way

        for i in range(m):
            # Traverse backwards to avoid overwriting values from the previous row
            for j in range(n - 1, -1, -1):
                if s[i] == t[j]:
                    dp[j + 1] += dp[j]

        return dp[n]

        