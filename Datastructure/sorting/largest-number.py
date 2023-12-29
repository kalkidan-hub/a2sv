class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if set(nums) == {0}:
            return str(0)
        nums = [str(num) for num in nums]
        # bubble it is
        for i in range(len(nums)):
            for j in range(1,len(nums)):
                if nums[j] + nums[j-1] > nums[j-1] + nums[j]:
                    nums[j], nums[j-1] = nums[j-1],nums[j]
        # print(nums)


        return "".join(nums)