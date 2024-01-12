class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # fixed size sliding window

        n,k = len(s2),len(s1)
        
        s1_ct = [0]*26
        window_ct = [0]*26

        for c in s1:
            s1_ct[ord(c)-97] += 1 
        for c in s2[:k]:
            window_ct[ord(c)-97] += 1
            
        
        for i in range(n-k):
            if s1_ct == window_ct:
                return True
            window_ct[ord(s2[i])-97] -= 1
            window_ct[ord(s2[i+k])-97] += 1

        return s1_ct == window_ct
           


