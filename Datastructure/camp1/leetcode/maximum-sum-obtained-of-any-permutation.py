class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:

        # trace the frequency of the indexes
        freq_tracer = [0]*(len(nums) + 1)

        for req in requests:
            freq_tracer[req[0]] += 1
            freq_tracer[req[1] + 1] -= 1
        
        frq_sum = [0]
        for fr in freq_tracer:
            frq_sum.append(frq_sum[-1] + fr)
        
        frq_sum = frq_sum[1:-1]
        
        # maintain the permutation where the values of the nums are placed in such a way that if we sort the frq_sum and nums
        # with their index goes attached to the value, we end up getting the exact same index distribution,


        # frq_sum and nums transformation

        frq_sum = sorted(list(enumerate(frq_sum)), key= lambda x:x[1])
        nums = sorted(list(enumerate(nums)), key= lambda x:x[1])



        new_nums = [0]*len(nums) # the permutation of nums that maximizes our request

        for i in range(len(nums)):
            new_nums[frq_sum[i][0]] = nums[i][1]

        # calculate the prefix sum of the new_nums and get the result

        prf_sum = [0]
        for p in new_nums:
            prf_sum.append(prf_sum[-1] + p)

        total = 0
        
        for req in requests:
            total += (prf_sum[req[1] + 1] - prf_sum[req[0]])
    
        return total%(10**9 + 7)