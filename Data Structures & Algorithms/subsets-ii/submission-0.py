from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        # 1. Sort the array so that duplicates are adjacent
        nums.sort() 
        
        def backtrack(start_index: int, path: List[int]):
            # Every state reached in the decision tree is a valid subset
            res.append(list(path))
            
            for i in range(start_index, len(nums)):
                # 2. Skip duplicates: if the current element is the same as the previous 
                # element AND it's not the first element in this recursive level.
                if i > start_index and nums[i] == nums[i - 1]:
                    continue
                
                # Make choice
                path.append(nums[i])
                # Move to next element
                backtrack(i + 1, path)
                # Backtrack (undo choice)
                path.pop()
        
        backtrack(0, [])
        return res

        