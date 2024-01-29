class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def atmostKodd(nums,k):
            i,j = 0,0
            ct = 0
            while j < len(nums):
                if nums[j] & 1:
                    k -= 1
                while k < 0:
                    k += nums[i] & 1
                    i += 1
                ct += j-i + 1
                j += 1
            return ct

        return atmostKodd(nums,k) - atmostKodd(nums,k-1)
                


                