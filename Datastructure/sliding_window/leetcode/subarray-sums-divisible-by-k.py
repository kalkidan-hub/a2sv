class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prf_moded = [0]
        for num in nums:
            prf_moded.append(prf_moded[-1] + num) 
        prf_moded = [i%k for i in prf_moded]
        
        prev_poss = {}
        res = 0
        for k in prf_moded:
            if k in prev_poss:
                res += prev_poss[k]
                prev_poss[k] += 1
            else:
                prev_poss[k] = 1
        
        return res
            
        