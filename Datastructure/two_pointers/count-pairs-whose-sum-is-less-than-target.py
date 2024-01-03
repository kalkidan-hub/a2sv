class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        ct = 0
        nums.sort()
        i,j = 0,len(nums)-1
        while i < j:
            s = nums[i] + nums[j]
            if s >= target:
                j -= 1
            else:
                ct += (j-i)
                i += 1
        return ct
            