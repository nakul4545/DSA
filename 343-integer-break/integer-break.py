class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n - 1

        threes, remainder = divmod(n, 3)

        if remainder == 1:
            return 3 ** (threes - 1) * 4
        if remainder == 2:
            return 3 ** threes * 2
        return 3 ** threes
