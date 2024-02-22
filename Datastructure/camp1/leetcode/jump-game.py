class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        j, i = len(nums) - 1, len(nums) - 2
        while i >= 0:
            while j - i > nums[i] and i >= 0:
                i -= 1
            if i < 0:
                return False    
            j = i
            i -= 1
        return True