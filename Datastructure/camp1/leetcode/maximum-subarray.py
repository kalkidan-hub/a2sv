class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        _min = 10001
        max_sum = -10001

        curr_sum = 0
        for i in range(len(nums)):

            _min = min(_min,curr_sum)
            curr_sum += nums[i]
            max_sum = max(max_sum,curr_sum - _min)
            

        return max_sum


        