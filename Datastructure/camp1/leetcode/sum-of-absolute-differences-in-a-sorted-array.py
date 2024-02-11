class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        _sum = sum(nums) # final variable # O(n)
        left = 0 # to store running sum 

        result = []
        n = len(nums)

        # O(n)
        for i in range(n):
            res = (nums[i]*i - left) + ((_sum - left) - nums[i]*(n-i)) # O(1)
            result.append(res) # O(1)
            left += nums[i] # O(1)

        # O(2n) = O(n)
        
        return result        