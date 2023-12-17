class ATM:

    def __init__(self):
        self.notes_freq = defaultdict(int)
        self.notes = [20,50,100,200,500]
        

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(len(banknotesCount)):
            self.notes_freq[i] += banknotesCount[i]
        # print(self.notes_freq)

    def withdraw(self, amount: int) -> List[int]:
        withdrawal = defaultdict(int)
        safe = True
        for i in range(4,-1,-1):
            if not self.notes_freq[i]:
                continue                
            withdrawal[i] = min(self.notes_freq[i],amount//self.notes[i])
            amount -= withdrawal[i] * self.notes[i] 
        # print(withdrawal,safe)
        if not amount and safe:
            self.notes_freq = {note:self.notes_freq[note] - withdrawal[note] for note in self.notes_freq}
            return [withdrawal[i] for i in range(5)]
        else:
            return [-1]


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)