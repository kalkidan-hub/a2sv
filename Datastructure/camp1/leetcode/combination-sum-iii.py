class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        curr = []
        
        def backtrack(i,_sum):

            if i > 9: 
                if len(curr) == k and _sum == n:
                    ans.append(curr.copy())
                return 
                
            if _sum <= n:
                curr.append(i)
                backtrack(i + 1,_sum + i)
                curr.pop()
                backtrack(i + 1,_sum)
        backtrack(1,0)

        return ans