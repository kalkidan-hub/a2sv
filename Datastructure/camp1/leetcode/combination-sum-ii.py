class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()
        path = []
        ans = []

        def backtrack(idx,_sum):
            if idx == len(candidates) or _sum >= target:
                if _sum == target:
                    ans.append(path.copy())
                return 
            
            nx = idx + 1
            while nx < len(candidates) and candidates[idx] == candidates[nx]:
                nx += 1
            path.append(candidates[idx])
            backtrack(idx+1, _sum + candidates[idx])
            path.pop()
            backtrack(nx,_sum)

        backtrack(0,0)
        return ans           