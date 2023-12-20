class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:

        global_count = Counter(nums)
        fresh_count = {0:0,1:0}
        res = [0]*(len(nums) + 1)
        
        # initial 
        res[0] = global_count[1]

        # keep going
        for i in range(len(nums)):
            if nums[i]:
                fresh_count[1] += 1
            else:
                fresh_count[0] += 1

            res[i+1] = fresh_count[0] + global_count[1] - fresh_count[1]
        
        max_score = max(res)
        actl_res = []

        for j in range(len(res)):
            if res[j] == max_score:
                actl_res.append(j)
                
        return actl_res
