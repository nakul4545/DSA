class Solution:
    def numSplits(self, s: str) -> int:
        left = set()
        right = {}

        for ch in s:
            right[ch] = right.get(ch, 0) + 1

        ans = 0

        for i in range(len(s) - 1):
            ch = s[i]

            left.add(ch)
            right[ch] -= 1

            if right[ch] == 0:
                del right[ch]

            if len(left) == len(right):
                ans += 1

        return ans