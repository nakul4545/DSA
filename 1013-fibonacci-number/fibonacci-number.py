class Solution:
    def fib(self, n: int) -> int:
        def fun(n):
            if n==0:
                return 0
            elif n == 1 or n ==2 :
                return 1
            ans = fun(n-1) + fun(n-2)
            return ans 
        x = fun(n)
        return x
