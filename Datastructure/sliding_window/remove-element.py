class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        w,ct = 0,0
        for r in range(len(nums)):
            if nums[r] != val:
                ct += 1
                nums[w],nums[r] = nums[r],nums[w]
                w += 1
        return ct