class MinStack:

    def __init__(self):
        self.stack=[]
        self.min=[]
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min) == 0:
            self.min.append(val)
        elif val<=self.min[-1]:
            self.min.append(val)

    def pop(self) -> None:
        if self.stack.pop()==self.min[-1]:
            self.min.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]


# Your MinStack object will be instantiated and called as such:

def minStack(operations:list,myStack:list):
    list_result=[]
    q=MinStack()
    for i in range(len(operations)):
        if operations[i]=='MinStack':
            list_result+=[None]
        elif operations[i]=='push':
            q.push(myStack[i][0])
            list_result+=[None]
        elif operations[i] == 'pop':
            list_result += [q.pop()]
        elif operations[i] == 'top':
            list_result += [q.top()]
        elif operations[i]=='getMin':
            list_result+=[q.getMin()]


    return list_result