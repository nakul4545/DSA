
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        if len(timePoints) > 1440:
            return 0

        seen = [False] * 1440

        for time in timePoints:
            h, m = map(int, time.split(":"))
            minutes = h * 60 + m

            if seen[minutes]:
                return 0

            seen[minutes] = True

        first = -1
        prev = -1
        ans = 1440

        for i in range(1440):
            if seen[i]:
                if first == -1:
                    first = i

                if prev != -1:
                    ans = min(ans, i - prev)

                prev = i

        ans = min(ans, 1440 - prev + first)
        return ans
