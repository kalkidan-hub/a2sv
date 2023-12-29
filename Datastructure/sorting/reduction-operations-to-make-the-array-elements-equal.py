class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
       
        nums.sort(reverse=True)
        opn,i = 0,0

        while i < len(nums)-1:
            if nums[i] != nums[i+1]:
                opn += (i + 1)
            i += 1
        return opn