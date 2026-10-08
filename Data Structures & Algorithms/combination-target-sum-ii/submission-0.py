class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        # 1. Sort the candidates to make it easy to skip duplicate combinations
        candidates.sort()
        
        def backtrack(start: int, target: int, current_path: list[int]):
            # Base Case: Found a valid combination
            if target == 0:
                res.append(list(current_path))
                return
            
            # Iterate through the choices starting from the 'start' index
            for i in range(start, len(candidates)):
                # Early Pruning: If the current number is greater than the remaining target,
                # then all subsequent numbers will also be greater (since the array is sorted).
                if candidates[i] > target:
                    break
                
                # Duplicate Mitigation: Skip the same element if it's at the same recursive level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                # Make choice
                current_path.append(candidates[i])
                
                # Explore further (move to i + 1 as each number can only be used once)
                backtrack(i + 1, target - candidates[i], current_path)
                
                # Backtrack / Undo choice
                current_path.pop()
                
        backtrack(0, target, [])
        return res

        