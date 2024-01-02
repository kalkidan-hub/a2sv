class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # snowball approach,
        snow_ball_size = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                snow_ball_size += 1
            elif snow_ball_size:
                nums[i-snow_ball_size] = nums[i]
                nums[i] = 0
        