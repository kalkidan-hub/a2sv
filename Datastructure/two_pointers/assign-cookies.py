class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        
        i = j = ct = 0
        
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                ct += 1
                i,j = i+1, j+1
            else:
                j += 1
        
        
        return ct