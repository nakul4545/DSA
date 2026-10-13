class Solution:
    def countSegments(self, s: str) -> int:
        if s == "":
            return 0
        x = s.split()
        return len(x)