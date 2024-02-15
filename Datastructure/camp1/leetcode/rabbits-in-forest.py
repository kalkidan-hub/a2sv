class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        frq = Counter(answers)
        rabbits = 0
        for f in frq:
            rabbits += (f+1)*(math.ceil(frq[f]/(f+1)))
        return rabbits        