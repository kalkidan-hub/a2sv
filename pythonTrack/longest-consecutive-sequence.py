class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        ct = 0
        
        while s:
            curr = s.pop()
            curr_ct = 1
            _next = curr + 1
            while _next in s:
                curr_ct += 1
                s.remove(_next)
                _next += 1
            back_next = curr - 1
            while back_next in s:
                curr_ct += 1
                s.remove(back_next)
                back_next -= 1
            ct = max(ct,curr_ct)

        return ct
            
        