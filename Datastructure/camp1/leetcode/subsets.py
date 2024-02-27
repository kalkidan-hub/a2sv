class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        soln = []
        def backtrack(idx,path):
            if idx == len(nums):
                soln.append(path.copy())
                return        
            backtrack(idx + 1,path + [nums[idx]])
            backtrack(idx + 1,path)
            
        backtrack(0,[])
        return soln
        