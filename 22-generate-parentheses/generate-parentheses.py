class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def fun(openn, close, n,tmp, res):
            if openn == n and close == n:
                res.append("".join(tmp))
                return 
            if openn < n:
                tmp.append("(")
                fun(openn + 1, close, n , tmp, res)
                tmp.pop() # To check other condition

            if close < openn:
                tmp.append(")")
                fun(openn, close + 1, n , tmp, res)
                tmp.pop()
            
        res = []
        fun(0,0,n,[],res)
        return res

