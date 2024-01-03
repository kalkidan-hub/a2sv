class Solution:
    def isPalindrome(self, s: str) -> bool:
        the_str = [i.lower() for i in s if (97 <= ord(i.lower())<= 122) or (48 <= ord(i) <= 57)]
        
        is_pali = ''.join(the_str)
        the_str.reverse()
        is_it = ''.join(the_str)
        
        return is_pali == is_it