class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        def move_zzeros():
            nonlocal nums
            w = 0
            for r in range(len(nums)):
                if nums[r] != 101:
                    nums[w],nums[r] = nums[r],nums[w]
                    w += 1
        i,j = 0,1
        while j < len(nums):
            if nums[j] == nums[i]:
                nums[j] = 101
            else:
                i = j
            j += 1

        sub = nums.count(101)
        move_zzeros()

        return len(nums) - sub
