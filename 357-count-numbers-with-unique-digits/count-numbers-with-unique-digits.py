class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1

        total = 10
        count = 9

        for length in range(2, n + 1):
            count *= 11 - length
            total += count

        return total
