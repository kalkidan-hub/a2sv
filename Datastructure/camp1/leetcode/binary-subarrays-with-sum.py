class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # prefix sum approach 

        # use a dictionary to store a history,

        history = {0:1}
        running_sum = 0
        valid_subarrays = 0

        for n in nums:
            running_sum += n
            if (running_sum - goal) in history:
                valid_subarrays += history[(running_sum - goal)]
            # updating history
            if running_sum in history:
                history[running_sum] += 1
            else:
                history[running_sum] = 1
        return valid_subarrays