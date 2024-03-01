class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        if n == 0:
            return False
        elif (n%3 == 0):
            return True and self.isPowerOfThree(n//3)