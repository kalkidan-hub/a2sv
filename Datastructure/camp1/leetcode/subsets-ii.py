class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        subsets = []
        subset = []

        def backtrack(idx):
            if idx == len(nums):
                subsets.append(subset.copy())
                return
            nx = idx + 1
            while nx < len(nums) and nums[idx] == nums[nx]:
                nx += 1
            
            subset.append(nums[idx])
            backtrack(idx + 1)
            subset.pop()
            backtrack(nx)
        
        backtrack(0)
        return subsets