class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        d = {}
        j = 0
        for i in range(len(s)):
            
            if s[i] not in d:
                d[s[i]] = i
            else:
                l = max(l,i-j)
                v = (d[s[i]] + 1)
                while j < v:
                    del d[s[j]]
                    j += 1
                d[s[i]] = i
                
        l = max(l,len(d))
        return l if l else len(s)