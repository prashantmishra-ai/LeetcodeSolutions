class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()

        # Initialize the minimum sum as a large number
        min_sum = float('inf')

        # Loop through each pair of chocolates
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                # Calculate the sum of the two chocolates
                sum_of_two = prices[i] + prices[j]

                # Check if this sum is less than the current minimum and can be bought with the money available
                if sum_of_two < min_sum and sum_of_two <= money:
                    min_sum = sum_of_two

        # If a pair was found, return the leftover money, otherwise return the initial amount of money
        return money - min_sum if min_sum != float('inf') else money