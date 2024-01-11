class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zero_ct,i,res = 0,0,0

        for j in range(len(nums)):

            zero_ct += (nums[j] == 0)
            while zero_ct > k:
                zero_ct -= (nums[i] == 0)
                i += 1
            res = max(res,j-i+1)

        return res
