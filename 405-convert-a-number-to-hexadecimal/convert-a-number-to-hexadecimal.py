
class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"

        num = num & 0xFFFFFFFF
        chars = "0123456789abcdef"
        result = ""

        while num > 0:
            result = chars[num & 15] + result
            num >>= 4

        return result
