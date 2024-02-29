class Solution:
    def longestNiceSubstring(self, s: str) -> str:

        def solve(s):
            if len(s) <= 1:
                return ""

            elem = set(list(s))
            
            for i in range(len(s)):
                ch = s[i]
                if chr(ord(ch) + 32) in elem or chr(ord(ch) - 32) in elem:
                    continue
                else:
                    left, right = solve(s[:i]), solve(s[i + 1:])

                    return left if len(left) >= len(right) else right
            else:
                return s

        
        return solve(s)