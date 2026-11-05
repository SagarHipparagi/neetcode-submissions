from typing import List


class Solution:

  def change(self, amount: int, coins: List[int]) -> int:
    # Initialize a 1D DP array with zeros.
    # dp[i] will store the number of combinations to make amount `i`.
    dp = [0] * (amount + 1)

    # Base case: There is 1 way to make amount 0 (by using no coins).
    dp[0] = 1

    # Iterate through each coin denomination
    for coin in coins:
      # Update the dp array for all amounts from 'coin' up to 'amount'
      for i in range(coin, amount + 1):
        dp[i] += dp[i - coin]

    return dp[amount]

        