class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # calculate the number of windows whose sum is less than the goal 
        # and whose sum is less than (goal-1) then substract these two to get the windows whose sum is exactly goal

        def sum_less_than(goal):
            nonlocal nums
            _sum, i = 0, 0
            total = 0

            for j in range(len(nums)):
                _sum += nums[j]

                while i < len(nums) and _sum > goal:
                    _sum -= nums[i]
                    i += 1

                total += j - i + 1
            return total

        # print(sum_less_than(-1))
        return sum_less_than(goal) - sum_less_than(goal-1) if goal else sum_less_than(goal)

                



