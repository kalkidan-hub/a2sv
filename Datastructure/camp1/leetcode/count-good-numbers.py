class Solution:
    def countGoodNumbers(self, n: int) -> int:

        M = 10**9 + 7
        def myPow(x,n):
            nonlocal M
            if n == 0:
                return 1

            if x == 0:
                return 0

            if n%2:
                return x * myPow(x*x%M,n//2) % M
            else:
                return myPow(x*x%M,n//2) % M
        
        
        if n%2:
            return ((myPow(5,n//2+1) % M) * (myPow(4,n//2) % M))%M
        else:
            return ((myPow(5,n//2) % M)*(myPow(4,n//2) % M))%M