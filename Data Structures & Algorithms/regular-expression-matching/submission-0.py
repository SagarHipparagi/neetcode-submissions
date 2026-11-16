class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        
        # dp[i][j] will be True if s[:i] matches p[:j]
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        
        # Empty string matches empty pattern
        dp[0][0] = True
        
        # Handle patterns like a*, a*b*, or a*b*c* that can match an empty string
        for j in range(2, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]
                
        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                    # Current characters match directly
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    # Case 1: '*' matches zero occurrences of the preceding element
                    dp[i][j] = dp[i][j - 2]
                    
                    # Case 2: '*' matches one or more occurrences if preceding char matches s[i-1]
                    if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                        dp[i][j] = dp[i][j] or dp[i - 1][j]
                        
        return dp[m][n]


        