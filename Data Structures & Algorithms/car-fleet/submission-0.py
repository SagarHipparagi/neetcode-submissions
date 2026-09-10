class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # Pair position and speed, then sort by position in descending order
        cars = sorted(zip(position, speed), reverse=True)
        
        stack = []
        for p, s in cars:
            # Calculate time to reach the target
            time_to_target = (target - p) / s
            
            # If stack is empty or this car takes longer than the fleet ahead
            if not stack or time_to_target > stack[-1]:
                stack.append(time_to_target)
                
        return len(stack)
