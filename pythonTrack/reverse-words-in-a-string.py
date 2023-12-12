class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        res = ""
        for i in range(len(words)-1,-1,-1):
            if words[i]:
                res += words[i] + " "
        return res.strip()
