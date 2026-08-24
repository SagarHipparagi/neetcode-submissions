class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0

        for i in range(32):
            # Get the last bit of n
            bit = n & 1

            # Shift result left and add the bit
            result = (result << 1) | bit

            # Move to the next bit
            n = n >> 1

        return result