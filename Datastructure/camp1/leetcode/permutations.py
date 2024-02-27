class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        permutations = []
        perm = []

        def backtrack():
            if len(perm) == len(nums):
                permutations.append(perm.copy())
                return 
            for nx in nums:
                if nx not in perm:
                    perm.append(nx)
                    backtrack()
                    perm.pop()
        backtrack()
        return permutations