class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:

        # array manipulation where we need to update multiple entries by some suffix
        # in here the queries looks like (0,i,shifts[i]), 
        # where 0 is the left, i is the right and shifts[i]  is the value we need to suffix

        # lets numerize our string
        s = [ord(st)-97 for st in s]

        # finding summary of our operation
        opn = [0] * (len(s) + 1)

        for i in range(len(shifts)):
            opn[0] += shifts[i]
            opn[i+1] -= shifts[i]
        prf_sum = [0]
        for o in opn:
            prf_sum.append(prf_sum[-1] + o)

        i = 0
        for op in prf_sum[1:-1]:
            s[i] = (s[i] + op)%26
            i += 1

        return "".join([chr(97 + c) for c in s])