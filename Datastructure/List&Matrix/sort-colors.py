class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # selection sort, 
        w = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                nums[w],nums[r] = nums[r],nums[w]
                w += 1
                
        w = len(nums)-1
        for r in range(len(nums)-1,-1,-1):
            if nums[r] == 2:
                nums[w],nums[r] = nums[r],nums[w]
                w -= 1
            
                