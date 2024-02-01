class Solution:
    def minWindow(self, s: str, t: str) -> str:
        rec = Counter(t)
        res = s + "a"
        i = 0
        for j in range(len(s)):
            if s[j] in rec:
                rec[s[j]] -= 1
            while all(rec[v] <= 0 for v in rec):
                if j - i + 1 < len(res):
                    res = s[i:j+1]
                if s[i] in rec:
                    rec[s[i]] += 1
                i += 1
        return res if res != s + "a" else ""
            