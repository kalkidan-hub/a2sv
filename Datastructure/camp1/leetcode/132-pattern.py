class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        # while building the monotonic stack
        mono_stack = []
        curr_min = nums[0]
        for i in range(1,len(nums)):

            while mono_stack and mono_stack[-1][0] <= nums[i]:
                mono_stack.pop()

            if mono_stack and nums[i] > mono_stack[-1][1]:
                return True
            
            mono_stack.append([nums[i],curr_min])
            curr_min = min(curr_min,nums[i])