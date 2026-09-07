class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dictt={
            "2" : ["a","b",'c'],
            "3": ["d","e","f"],
            "4": ["g","h","i"],
            "5": ["j","k","l"],
            "6": ["m","n","o"],
            "7": ["p","q","r","s"],
            "8": ["t","u","v"],
            "9": ["w","x","y","z"]
        }
        if not digits:
            return []
        res = []
        def backtrack(index, path,res):
            if index == len(digits):
                res.append("".join(path))
                return 
            for ch in dictt[digits[index]]:
                path.append(ch)
                backtrack(index+1, path, res)
                path.pop()
        backtrack(0, [], res)
        return res
            