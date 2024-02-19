class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # have an array concatenated with itself, so that we don't lose the circularity
        nums = nums*2
        # perform the usual monotonicity, capturing the indices in the dictionary
        dic = {}
        mono_stack = []

        for i in range(len(nums)):
            while mono_stack and nums[mono_stack[-1]] < nums[i]:
                dic[mono_stack.pop()] = i
            mono_stack.append(i)
        res = []
        for j in range(len(nums)//2):
            if j in dic:
                res.append(nums[dic[j]%len(nums)])
            else:
                res.append(-1)

        return res       