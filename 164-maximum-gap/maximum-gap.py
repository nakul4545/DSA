class Solution:
    def maximumGap(self, nums: list[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0

        low, high = min(nums), max(nums)
        if low == high:
            return 0

        width = max(1, (high - low + n - 2) // (n - 1))
        count = (high - low) // width + 1
        bucket_min = [float("inf")] * count
        bucket_max = [float("-inf")] * count

        for value in nums:
            index = (value - low) // width
            bucket_min[index] = min(bucket_min[index], value)
            bucket_max[index] = max(bucket_max[index], value)

        answer = 0
        previous_max = low

        for index in range(count):
            if bucket_min[index] == float("inf"):
                continue
            answer = max(answer, bucket_min[index] - previous_max)
            previous_max = bucket_max[index]

        return answer
