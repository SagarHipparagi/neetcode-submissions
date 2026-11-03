class Solution:
  def maxProfit(self, prices: list[int]) -> int:
    if not prices:
      return 0

    # Initialize state variables for the first day
    sold = 0
    cooldown = 0
    hold = -prices[0]

    for price in prices[1:]:
      prev_sold = sold
      sold = hold + price
      hold = max(hold, cooldown - price)
      cooldown = max(cooldown, prev_sold)

    return max(sold, cooldown)

        