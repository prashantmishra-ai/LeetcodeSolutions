class Solution:
    def totalMoney(self, n: int) -> int:
        total = 0
        week = 0
        for i in range(1, n + 1):
            if i % 7 == 1:
                week += 1
            total += week + (i - 1) % 7
        return total