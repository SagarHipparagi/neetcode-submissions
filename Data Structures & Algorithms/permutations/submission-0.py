from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def backtrack(current_path, visited):
            # Base Case: If the path length matches the input length, 
            # we found a full permutation.
            if len(current_path) == len(nums):
                result.append(list(current_path)) # Append a copy of the path
                return
            
            # Recursive Step: Try every available number
            for num in nums:
                if num not in visited:
                    # Take: add to path and mark as visited
                    current_path.append(num)
                    visited.add(num)
                    
                    # Explore next decisions
                    backtrack(current_path, visited)
                    
                    # Clean up / Backtrack: undo our decision
                    visited.remove(num)
                    current_path.pop()

        # Kick off backtracking with an empty path and an empty tracking set
        backtrack([], set())
        return result

# --- Local Testing Code ---
if __name__ == "__main__":
    # 1. Instantiate the class
    solution = Solution()
    
    # 2. Provide test input
    test_nums = [1, 2, 3]
    
    # 3. Execute and print output
    print(solution.permute(test_nums))


        