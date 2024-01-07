class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        p1, p2 = 0,k
        max_sum,prev_sum = sum(nums[:k]),sum(nums[:k])
        while p2 < len(nums):
            
            curr_sum = prev_sum - nums[p1] + nums[p2]
            max_sum = max(max_sum,curr_sum)
            prev_sum = curr_sum
            p1 += 1
            p2 += 1
        return max_sum/k
            
