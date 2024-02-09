class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        kick_off = {val:0 for val in set(nums)}
        total_ct = 0

        i = 0
        for j in range(len(nums)):
            kick_off[nums[j]] += 1
            while all(kick_off[v] for v in kick_off):
                total_ct += len(nums) - j
                kick_off[nums[i]] -= 1
                i += 1
        
        return total_ct
