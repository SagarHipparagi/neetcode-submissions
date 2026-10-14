class Solution:
    def partition(self, s: str) -> list[list[str]]:
        result = []
        current_partition = []
        
        def is_palindrome(left: int, right: int) -> bool:
            # Check if substring s[left:right+1] is a palindrome
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        def backtrack(start_idx: int):
            # Base Case: If we reach the end of the string, a valid partition is found
            if start_idx >= len(s):
                result.append(current_partition.copy())
                return
            
            # Explore all possible substrings starting from 'start_idx'
            for end_idx in range(start_idx, len(s)):
                if is_palindrome(start_idx, end_idx):
                    # Choose: Add the palindromic substring to the current track
                    current_partition.append(s[start_idx : end_idx + 1])
                    
                    # Explore: Recursively check the rest of the string
                    backtrack(end_idx + 1)
                    
                    # Backtrack: Undo the choice for the next loop iteration
                    current_partition.pop()

        # Start backtracking from index 0
        backtrack(0)
        return result

# Example usage:
if __name__ == "__main__":
    sol = Solution()
    print(sol.partition("aab"))
    # Output: [['a', 'a', 'b'], ['aa', 'b']]

        