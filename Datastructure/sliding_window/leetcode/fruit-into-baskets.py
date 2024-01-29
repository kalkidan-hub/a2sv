class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = collections.defaultdict(int)
        i, total, res = 0,0,0
        
        for r in range(len(fruits)):
            count[fruits[r]] += 1
            total += 1
            
            while len(count) > 2:
                f = fruits[i]
                count[f] -= 1
                total -= 1
                i += 1
                if not count[f]:
                    count.pop(f)
                
                    
            res = max(res,total)
            
            
        return res