class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        reach, idx, x = 0, 0, 1
        patches = 0
        while reach < n:
            print(reach,idx,x)
            if idx < len(nums) and nums[idx] <= x:
                reach += nums[idx]
                idx += 1
                x = reach + 1
            else:
                reach += x
                patches += 1
                x = reach + 1
        
        return patches