

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # Use hash sets to track seen numbers for rows, columns, and 3x3 boxes
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        boxes = collections.defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                
                # Skip empty cells indicated by a period
                if val == '.':
                    continue
                
                # Calculate the 3x3 box index coordinate
                box_idx = (r // 3, c // 3)
                
                # If the value already exists in the same row, column, or box, it's invalid
                if (val in rows[r] or 
                    val in cols[c] or 
                    val in boxes[box_idx]):
                    return False
                
                # Map the current value into the tracking sets
                rows[r].add(val)
                cols[c].add(val)
                boxes[box_idx].add(val)
                
        return True
import collections

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # Use hash sets to track seen numbers for rows, columns, and 3x3 boxes
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        boxes = collections.defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                
                # Skip empty cells indicated by a period
                if val == '.':
                    continue
                
                # Calculate the 3x3 box index coordinate
                box_idx = (r // 3, c // 3)
                
                # If the value already exists in the same row, column, or box, it's invalid
                if (val in rows[r] or 
                    val in cols[c] or 
                    val in boxes[box_idx]):
                    return False
                
                # Map the current value into the tracking sets
                rows[r].add(val)
                cols[c].add(val)
                boxes[box_idx].add(val)
                
        return True
