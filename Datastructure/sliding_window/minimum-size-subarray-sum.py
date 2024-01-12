class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        '''
        2 3 5 2 4 3      _sum = 8, _min = 2
          |
              |
        '''
        i,_sum,_min = 0,0,inf
        for j in range(len(nums)):
            _sum += nums[j]
            while _sum >= target:
                _min = min(_min,j-i+1)
                _sum -= nums[i]
                i += 1

        return 0 if _min == inf else _min