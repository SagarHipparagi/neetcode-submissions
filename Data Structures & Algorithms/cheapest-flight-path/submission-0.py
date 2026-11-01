class Solution:
    def findCheapestPrice(
        self, n: int, flights: list[list[int]], src: int, dst: int, k: int
    ) -> int:
        # Initialize distance array with infinity for all cities
        prices = [float("inf")] * n
        prices[src] = 0

        # At most k stops mean at most k + 1 flights
        for _ in range(k + 1):
            temp_prices = prices.copy()

            for u, v, price in flights:
                # If city 'u' is unreachable, skip
                if prices[u] == float("inf"):
                    continue
                # Relax the edge using prices from the previous iteration
                if prices[u] + price < temp_prices[v]:
                    temp_prices[v] = prices[u] + price

            prices = temp_prices

        return prices[dst] if prices[dst] != float("inf") else -1

        