class RandomizedSet:

    def __init__(self):
       self.randSet = {}
       self.randList = list()

    def insert(self, val: int) -> bool:

        if val not in self.randSet:
            self.randSet[val] = len(self.randSet)
            self.randList.append(val)
            return True

    def remove(self, val: int) -> bool:
        # popping,
        if val in self.randSet:
            # get an index, 
            idx = self.randSet[val]
            
            # bring it to the end, 
            self.randSet[self.randList[-1]] = idx
            self.randList[idx], self.randList[-1] = self.randList[-1], self.randList[idx]
            del self.randSet[val]

            # what's left? of course, popping,,, 
            self.randList.pop() 
            return True       

    def getRandom(self) -> int:
        return random.choice(self.randList)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()