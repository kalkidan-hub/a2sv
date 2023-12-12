class OrderedStream:

    def __init__(self, n: int):
        self.leng = n
        self.stream = ['']*n
        self.occupied = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey-1] = value
        
        if idKey == self.occupied + 1:
            while self.occupied < self.leng and self.stream[self.occupied]:
                self.occupied += 1

        condition = idKey == 1 or self.occupied >= idKey
        res = []
        if condition:
            i = idKey - 1
            while i < self.leng and self.stream[i]:
                res.append(self.stream[i])
                i += 1
        return res
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)