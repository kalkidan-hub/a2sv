class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        _max = 0
        ct = 0
        for i,bit in enumerate(flips,1):
            _max = max(_max,bit)
            if _max == i:
                ct += 1
        return ct
