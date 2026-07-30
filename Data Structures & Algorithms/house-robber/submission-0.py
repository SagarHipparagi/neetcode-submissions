class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1 = 0
        rob2 = 0

        for money in nums:
            newRob = max(rob1 + money, rob2)
            rob1 = rob2
            rob2 = newRob

        return rob2