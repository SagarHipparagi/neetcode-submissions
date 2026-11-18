class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        while n != 1 and n not in seen:
            seen.add(n)
            n = self.sum_of_squares(n)
            
        return n == 1

    def sum_of_squares(self, n: int) -> int:
        total = 0
        while n > 0:
            digit = n % 10
            total += digit ** 2
            n //= 10
        return total

# Example usage:
sol = Solution()
print(sol.isHappy(100))  # True
print(sol.isHappy(101))  # False

        