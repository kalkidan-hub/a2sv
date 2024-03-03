class Solution:
    def kthGrammar(self, n: int, k: int) -> int:

        if n == 1:
            return 0
        parent = self.kthGrammar(n-1,math.ceil(k/2))

        if k%2 and parent:
            return 1
        elif not k%2 and parent:
            return 0
        
        elif k%2 and not parent:
            return 0
        else:
            return 1