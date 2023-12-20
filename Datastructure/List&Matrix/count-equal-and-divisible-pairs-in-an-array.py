class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        # brute force it is,,,,
        ct = 0

        for i in range(len(nums)):
            for j in range(i + 1,len(nums)):
                if (i*j) % k == 0 and nums[i] == nums[j]:
                    ct += 1

        return ct
