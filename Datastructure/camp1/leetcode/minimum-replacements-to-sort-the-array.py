class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        operations = 0
        bound = nums[-1]
        for i in range(len(nums)-1,-1,-1):
            if nums[i] > bound:

                spaces = math.ceil(nums[i]/bound)
                operations += spaces - 1
                bound = nums[i]//spaces
            else:
                bound = nums[i]

        return operations