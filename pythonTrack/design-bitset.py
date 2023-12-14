class Bitset:

    def __init__(self, size: int):
        self.bitset = [0]*size
        self.flipped = [1]*size
        self.countOne = 0
        self.size = size

    def fix(self, idx: int) -> None:
        if not self.bitset[idx]:
            self.bitset[idx] = 1
            self.countOne += 1
        if self.flipped[idx]:
            self.flipped[idx] = 0
        

    def unfix(self, idx: int) -> None:

        if self.bitset[idx]:
           self.bitset[idx] = 0
           self.countOne -= 1
        if not self.flipped[idx]:
            self.flipped[idx] = 1

    def flip(self) -> None:
        self.bitset, self.flipped = self.flipped, self.bitset
        self.countOne = self.size - self.countOne

    def all(self) -> bool:
        return self.countOne == self.size

    def one(self) -> bool:
        return not not self.countOne

    def count(self) -> int:
        return self.countOne

    def toString(self) -> str:
        return "".join([str(b) for b in self.bitset])


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()