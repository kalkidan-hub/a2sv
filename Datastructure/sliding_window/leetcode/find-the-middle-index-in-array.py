class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        prf_sum = [0]
        for i in nums:
            prf_sum.append(prf_sum[-1] + i)
        
        
        for s in range(len(prf_sum)-1):
            if prf_sum[s] == prf_sum[-1] - prf_sum[s+1]:
                return s
            
        
        return -1