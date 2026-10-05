class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = [[]]
        
        for num in nums:
            # Add the current number to all existing subsets
            res += [curr + [num] for curr in res]
            
        return res

        