class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # Quick length validation
        if len(s1) + len(s2) != len(s3):
            return False
            
        memo = {}
        
        def dfs(i: int, j: int) -> bool:
            # Base case: successfully matched all characters
            if i == len(s1) and j == len(s2):
                return True
                
            # Check cache
            if (i, j) in memo:
                return memo[(i, j)]
                
            k = i + j
            
            # Check matches against s1 and s2
            match_s1 = i < len(s1) and s1[i] == s3[k] and dfs(i + 1, j)
            match_s2 = j < len(s2) and s2[j] == s3[k] and dfs(i, j + 1)
            
            memo[(i, j)] = match_s1 or match_s2
            return memo[(i, j)]
            
        return dfs(0, 0)

# Optional entry point for standalone local testing
if __name__ == "__main__":
    solver = Solution()
    
    # Test Case 1: True
    res1 = solver.isInterleave("aabcc", "dbbca", "aadbbcbcac")
    print(f"Test 1 Passed: {res1 == True} (Result: {res1})")
    
    # Test Case 2: False
    res2 = solver.isInterleave("aabcc", "dbbca", "aadbbbaccc")
    print(f"Test 2 Passed: {res2 == False} (Result: {res2})")

