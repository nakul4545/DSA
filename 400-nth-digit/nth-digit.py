
class Solution:
    def findNthDigit(self, n: int) -> int:
        digit = 1
        count = 9
        start = 1

        # Step 1: Find the digit-length group
        while n > digit * count:
            n -= digit * count
            digit += 1
            count *= 10
            start *= 10

        # Step 2: Find the actual number
        num = start + (n - 1) // digit

        # Step 3: Find the digit inside that number
        index = (n - 1) % digit

        return int(str(num)[index])
