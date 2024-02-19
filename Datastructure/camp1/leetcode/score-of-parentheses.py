class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        for p in s:
            if p == '(':
                stack.append(0)
            else:
                top = stack.pop()
                # process the top
                val = max(1,top*2)
                stack[-1] += val
                
        return stack.pop()
        