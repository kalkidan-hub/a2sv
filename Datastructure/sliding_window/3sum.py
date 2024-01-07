class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        res = set()

        for i in range(len(nums)-1):
            l = i + 1
            r = len(nums) - 1

            while l < r:

                curr_sum = nums[i] + nums[l] + nums[r]
                if not curr_sum:
                    res.add((nums[i],nums[l],nums[r]))
                    l += 1
                    r -= 1
                elif curr_sum < 0:
                    l += 1
                else:
                    r -= 1

        res = list(list(triple) for triple in res)         
        return res 