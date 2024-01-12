class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        score = 0
        # a window of unique numbers with maximum sum 
        i,_sum = 0,0
        record = defaultdict(int)

        for j in range(len(nums)):
            while record[nums[j]] != 0:
                _sum -= nums[i]
                record[nums[i]] -= 1
                i += 1
            _sum += nums[j]
            record[nums[j]] += 1
            score = max(score,_sum)
        
        return score