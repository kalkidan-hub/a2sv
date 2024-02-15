class Solution:
    def longestPalindrome(self, s: str) -> int:
        ct = Counter(s)
        ans = 0
        no_odd = True
        for ch in ct:
            if ct[ch]%2 and no_odd:
                ans += ct[ch]
                no_odd = False
            else:
                ans += (ct[ch] - ct[ch]%2)

        return ans