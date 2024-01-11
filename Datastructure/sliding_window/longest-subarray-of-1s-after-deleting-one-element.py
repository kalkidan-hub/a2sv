class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        _range = []
        i,j = 0,0
        while j < len(nums):
            if nums[j] == 0:
                _range.append([i,j])
                j += 1
                i = j
            else:
                j += 1
        _range.append([i,j])
        res = _range[0][1] - _range[0][0] - 1
        
        for r in range(len(_range)-1):
            curr, nex = _range[r], _range[r+1]
            if  curr[1] + 1 == nex[0]:
                res = max(res,nex[1] - curr[0] - 1)

        return res
        