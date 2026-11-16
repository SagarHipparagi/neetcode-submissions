class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN = -2**31      # -2147483648
        INT_MAX = 2**31 - 1   #  2147483647
        
        sign = -1 if x < 0 else 1
        x = abs(x)
        reversed_num = 0
        
        while x != 0:
            digit = x % 10
            x //= 10
            
            # Check for 32-bit signed integer overflow before appending the digit
            if reversed_num > (INT_MAX - digit) // 10:
                return 0
                
            reversed_num = reversed_num * 10 + digit
            
        result = sign * reversed_num
        
        # Final boundary check for negative edge case (-2147483648)
        if result < INT_MIN or result > INT_MAX:
            return 0
            
        return result
