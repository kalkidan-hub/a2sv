class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:

        target = sum(nums) % p
        if target == 0:
            return 0

        hashset = {0:-1}
        prf_sum = 0
        subarray = len(nums)

        for i in range(len(nums)):

            prf_sum += nums[i]
            key = (prf_sum % p - target)%p

            if key in hashset:
                subarray = min(subarray,i - hashset[key])
            hashset[prf_sum % p] = i

        return subarray if subarray < len(nums) else -1