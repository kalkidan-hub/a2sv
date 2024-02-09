class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        ct = 0
        prf_sum = [0]
        ct_dic = {0:1}
        for i in nums:
            prf_sum.append(prf_sum[-1] + i)
            if prf_sum[-1] - goal in ct_dic:
                ct += ct_dic[prf_sum[-1] - goal]
            if prf_sum[-1] in ct_dic:
                ct_dic[prf_sum[-1]] += 1
            else:
                ct_dic[prf_sum[-1]] = 1
       
       
        return ct