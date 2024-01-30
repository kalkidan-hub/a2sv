class Solution:
    def balancedString(self, s: str) -> int:
        min_substring = len(s)
        count = Counter(s)
        ref = len(s)//4
        i = 0
        for j in range(len(s)):
            count[s[j]] -= 1
            while all(ct <= ref for ct in count.values()) and i < len(s):
                min_substring = min(min_substring,j-i+1)
                count[s[i]] += 1
                i += 1
                        
        return min_substring