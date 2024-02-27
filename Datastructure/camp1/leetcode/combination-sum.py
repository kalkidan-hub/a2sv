class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def backtrack(path,_sum):
            if _sum >= target:
                if _sum == target and sorted(path) not in ans:
                    ans.append(sorted(path.copy()))
                return 
            
            for nx in candidates:
                if _sum < target:
                    path.append(nx)
                    backtrack(path,_sum + nx)
                    path.pop()

        backtrack([],0)    
        return ans