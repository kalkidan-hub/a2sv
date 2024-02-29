class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        comb = []
        curr = []

        letter = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        def backtrack(idx):
            if idx == len(digits):
                if curr:
                    comb.append("".join(curr))
                return
            
            for nx in letter[digits[idx]]:
                curr.append(nx)
                backtrack(idx + 1)
                curr.pop()

        backtrack(0)
        return comb