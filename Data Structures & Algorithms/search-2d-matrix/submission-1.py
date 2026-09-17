class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        # Correctly check for empty matrix OR empty first row
        if not matrix or not matrix[0]:
            return False
            
        rows = len(matrix)
        cols = len(matrix[0])
        
        left = 0
        right = (rows * cols) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            # Map 1D index back to 2D matrix coordinates
            row_idx = mid // cols
            col_idx = mid % cols
            
            current_val = matrix[row_idx][col_idx]
            
            if current_val == target:
                return True
            elif current_val < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return False



