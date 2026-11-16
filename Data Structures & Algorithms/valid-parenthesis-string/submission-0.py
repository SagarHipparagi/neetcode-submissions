class Solution:
    def checkValidString(self, s: str) -> bool:
        low = 0   # Minimum possible unmatched '('
        high = 0  # Maximum possible unmatched '('
        
        for char in s:
            if char == '(':
                low += 1
                high += 1
            elif char == ')':
                low -= 1
                high -= 1
            else:  # char == '*'
                low -= 1   # Treat '*' as ')'
                high += 1  # Treat '*' as '('
                
            # Too many ')' encountered even if all '*' act as '('
            if high < 0:
                return False
                
            # Unmatched '(' count cannot drop below 0 (treat extra '*' as empty string)
            if low < 0:
                low = 0
                
        # Valid if it is possible to have 0 unmatched '(' at the end
        return low == 0

        