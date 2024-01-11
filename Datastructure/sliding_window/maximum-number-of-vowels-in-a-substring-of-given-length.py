class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        vowels = {'a','e','i','o','u'}
        max_vowel = sum(val in vowels for val in s[:k])
        prev_vowel = max_vowel

        print(prev_vowel)
        for i in range(len(s)-k):
            n_max = prev_vowel - (s[i] in vowels) + (s[i+k] in vowels)
            prev_vowel = n_max
            max_vowel = max(max_vowel,n_max)
        return max_vowel