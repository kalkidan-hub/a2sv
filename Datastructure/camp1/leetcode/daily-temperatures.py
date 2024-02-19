class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temperatures)
        
        for i in range(len(temperatures)):
            if not stack or stack[-1][0] > temperatures[i]:
                stack.append((temperatures[i],i))
            else:
                while stack and stack[-1][0] < temperatures[i]:
                    curr = stack.pop()
                    res[curr[1]] = i - curr[1]
                
                stack.append((temperatures[i],i))
        
        return res
                