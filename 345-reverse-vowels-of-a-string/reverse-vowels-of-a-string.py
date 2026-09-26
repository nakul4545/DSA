class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ["A","E","I","O","U","a","e","i","o","u"]
        s = list(s)
        low = 0 
        high = len(s) - 1
        while low < high:
            if s[low] in vowels and s[high] in vowels:
                s[low], s[high] = s[high], s[low]
                low += 1
                high -= 1
            elif s[high] not in vowels:
                high -= 1
            else:
                low += 1
        return "".join(s)
