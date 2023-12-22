class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        fir, sec = inf,inf
        for n in nums:
            if n <= fir:
                fir = n
            elif n <= sec:
                sec = n
            else:
                return True
        