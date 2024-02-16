class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        opn = 0
        stack = 0
        for p in s:
            if p == '(':
                stack += 1
            else:
                if not stack:
                    opn += 1
                else:
                    stack -= 1
        return opn + stack