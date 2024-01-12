class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        # falsify 
        res,true_ct,false_ct = 0,0,0
        i = 0
        for j in range(len(answerKey)):
            true_ct += (answerKey[j] == 'T')
            while true_ct > k:
                true_ct -= (answerKey[i] == 'T')
                i += 1
            res = max(res,j-i+1)
        
        # truezify 
        i = 0
        for j in range(len(answerKey)):
            false_ct += (answerKey[j] == 'F')
            while false_ct > k:
                false_ct -= (answerKey[i] == 'F')
                i += 1
            res = max(res,j-i+1)

        return res