class Solution:
    def minAreaRect(self, points: list[list[int]]) -> int:
        point_set = {tuple(point) for point in points}
        min_area = float("inf")

        for i, (x1, y1) in enumerate(points):
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]

                if x1 == x2 or y1 == y2:
                    continue

                if (x1, y2) in point_set and (x2, y1) in point_set:
                    area = abs(x2 - x1) * abs(y2 - y1)
                    min_area = min(min_area, area)

        return 0 if min_area == float("inf") else min_area