class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:

        min_max = nums[0]
        running_sum = 0
        
        for i in range(len(nums)):
            running_sum += nums[i]
            min_max = max(min_max,math.ceil(running_sum/(i+1)))

        return min_max