class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        total_customers = customers.count('Y')
        prefix_open_penalty = [0] * (n + 1)
        prefix_closed_penalty = [0] * (n + 1)

        for i in range(1, n + 1):
            prefix_open_penalty[i] = prefix_open_penalty[i - 1] + (customers[i - 1] == 'N')
            prefix_closed_penalty[i] = prefix_closed_penalty[i - 1] + (customers[i - 1] == 'Y')

        min_penalty = float('inf')
        min_hour = -1

        for hour in range(n + 1):
            open_penalty = prefix_open_penalty[hour]
            closed_penalty = total_customers - prefix_closed_penalty[hour]
            penalty = open_penalty + closed_penalty

            if penalty < min_penalty:
                min_penalty = penalty
                min_hour = hour

        return min_hour