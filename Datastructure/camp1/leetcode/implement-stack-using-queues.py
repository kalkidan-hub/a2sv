class MyStack:

    def __init__(self):
        self.queue = []  
        self.length = 0     

    def push(self, x: int) -> None:
        self.queue.append(x)
        self.length += 1       

    def pop(self) -> int:
        for _ in range(self.length - 1):
            elem = self.queue.pop(0)
            self.queue.append(elem)
        self.length -= 1
        return self.queue.pop(0)             

    def top(self) -> int:
        return self.queue[-1]

    def empty(self) -> bool:
        return self.length == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()