class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        # Phase 1: Find the intersection point of the tortoise and hare
        tortoise = nums[0]
        hare = nums[0]
        
        # Move hare 2 steps and tortoise 1 step until they meet
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break
        
        # Phase 2: Find the entrance to the cycle (the duplicate number)
        tortoise = nums[0]  # Reset tortoise to the beginning
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]  # Hare now moves at 1 step speed too
            
        return tortoise


        