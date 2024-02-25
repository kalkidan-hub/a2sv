class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [-1]*k
        self.size = k
        self.elements = 0
        self.start = 0
        self.end = -1        

    def enQueue(self, value: int) -> bool:
        if not self.isFull():
            nxt_pos = (self.end + 1) % self.size
            self.queue[nxt_pos] = value
            self.elements += 1
            self.end = nxt_pos
            return True

    def deQueue(self) -> bool:
        if not self.isEmpty():
            self.queue[self.start] = -1
            self.start = (self.start + 1) % self.size
            self.elements -= 1
            return True            
        

    def Front(self) -> int:
        return self.queue[self.start]        

    def Rear(self) -> int:
        return self.queue[self.end]
    def isEmpty(self) -> bool:
        return self.elements == 0
    def isFull(self) -> bool:
        return self.elements == self.size
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()