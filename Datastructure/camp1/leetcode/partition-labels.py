class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ans = []
        while s:
            i,j = 1, len(s) - 1
            for n in range(len(s)-1,-1,-1):
                if s[n] == s[0]:
                    prev_j = n
                    break
            while i < prev_j:
                if s[i] != s[j] and j > prev_j:
                    j -= 1
                else:
                    prev_j = j
                    i += 1
                    j = len(s) - 1
            ans.append(prev_j + 1)
            s = s[prev_j + 1:]
            
        return ans