class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        lst = list(range(1,n + 1))
        
        def combination(lst,k):
           
            # base case
            if k == 1:
                return [[i] for i in lst]
            if len(lst) == k:
                return [lst]
            
            # recursion case
            collective = []
            for i in range(len(lst)):
                temp_res = combination(lst[i + 1:],k-1)

                for j in temp_res:
                    j.append(lst[i])
                    collective.append(j)
            return collective
        
        
        return combinations(lst,k)