class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        # so this is why they called it shifting letters II
        # numerize the string

        s = [ord(c)-ord('a') for c in s]

        print(s)
        
        # getting our overall operation
        ops = [0]*(len(s) + 1)
        for sh in shifts:
            sh[2] = -1 if sh[2] == 0 else 1
            ops[sh[0]] += sh[2]
            ops[sh[1]+1] -= sh[2]
        prf_sum = [0]
        
        for op in ops:
            prf_sum.append(prf_sum[-1] + op)
        
        for i in range(len(s)):
            s[i] = (s[i] + prf_sum[i+1] )%26
        

        return "".join([chr(97 + c) for c in s])

