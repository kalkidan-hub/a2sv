class Solution:
    def isHappy(self, n: int) -> bool:
        unhappy = set()

        while n not in unhappy and n != 1:
            unhappy.add(n)
            num = str(n)
            n = sum([int(i)**2 for i in num])
        
        return n == 1