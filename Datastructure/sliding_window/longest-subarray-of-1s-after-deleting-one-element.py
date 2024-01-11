class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zero,i,res = -1,0,0

        for j in range(len(nums)):
            if nums[j] == 0 and zero != -1:
                res = max(res,j-i-1)
                i = zero + 1
                zero = j
            elif nums[j] == 0 and zero == -1:
                zero = j
        return max(res,j-i)
            
               

