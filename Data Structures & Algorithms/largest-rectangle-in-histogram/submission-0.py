class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []  # Stores indices of the bars
        max_area = 0
        # Append a dummy bar of height 0 to flush out remaining bars at the end
        heights.append(0) 
        
        for i in range(len(heights)):
            # While the current bar is shorter than the bar at the stack's top
            while stack and heights[i] < heights[stack[-1]]:
                height = heights[stack.pop()]
                # If stack is empty, it means the popped bar was the shortest so far
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
                
            stack.append(i)
            
        # Revert modification to the input array (good practice)
        heights.pop() 
        return max_area


        