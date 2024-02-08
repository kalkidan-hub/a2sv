class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res_count = 0
        counter = defaultdict(int)
        counter[0] = 1
        curr_sum = 0
        for i in range(len(nums)):
            curr_sum += nums[i]
            if (curr_sum - k) in counter:
                res_count += counter[curr_sum - k]
            counter[curr_sum] += 1
        return res_count
            
                