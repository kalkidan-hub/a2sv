class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:

        # the operation
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i + 1] = 0

        # the zero movement
        w = 0
        for r in range(len(nums)):
            if nums[r] != 0:
                nums[r], nums[w] = nums[w], nums[r]
                w += 1
        return nums


        
