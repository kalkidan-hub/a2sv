class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        tracker = defaultdict(int)
        i,res = 0,0
        for j in range(len(s)):
            tracker[s[j]] += 1
            while (j - i + 1 - max(tracker.values())) > k and i < len(s):
                tracker[s[i]] -= 1
                i += 1
            res = max(res,j-i+1)
        return res
            

        