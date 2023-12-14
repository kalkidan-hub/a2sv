class FrequencyTracker:

    def __init__(self):
        self.numCount = defaultdict(int)
        self.freqCount = defaultdict(int)
    def add(self, number: int) -> None:
        self.numCount[number] += 1
        
        curr = self.numCount[number]
        self.freqCount[curr-1] -= 1
        self.freqCount[curr] += 1
        
    def deleteOne(self, number: int) -> None:
        
        if self.numCount[number]:
            self.numCount[number] -= 1

            curr = self.numCount[number]
            self.freqCount[curr + 1] -= 1
            self.freqCount[curr] += 1 

    def hasFrequency(self, frequency: int) -> bool:
       
        return True if self.freqCount[frequency] else False
        

        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)