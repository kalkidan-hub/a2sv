class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]: 
        
        if len(p) > len(s):
            return []

        anagrams = []
        pc = [0]*26
        sc = [0]*26
        
        for c in range(len(p)):
            pc[ord(p[c])-97] += 1
            sc[ord(s[c])-97] += 1 
                     
        w = -1
        for w in range(len(s)-len(p)):
            if sc == pc:
                anagrams.append(w)
            sc[ord(s[w])-97] -= 1
            sc[ord(s[w+len(p)])-97] += 1
        
        if pc == sc :
            anagrams.append(w + 1)
        
        return anagrams
