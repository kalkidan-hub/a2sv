class Robot:

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.dir = 0
        self.moves = [
        [1,0],[0,1],[-1,0],[0,-1]
        ]
        self.pos = [0,0]
        self.dirMap = {0:"East",1:"North",2:"West",3:"South"}
    def valid(self, x,y):
        return 0 <= x < self.width and 0 <= y < self.height

    def step(self, num: int) -> None:

        num = num % ((self.width-1)*2 + (self.height-1)*2)
        if self.pos == [0,0]:
            self.dir = 3
        for i in range(num):

            newx,newy = self.pos[0] + self.moves[self.dir][0], self.pos[1]+self.moves[self.dir][1]

            if self.valid(newx,newy):
                self.pos = [newx,newy]
            else:            
                self.dir = (self.dir + 1)%4
                self.pos[0] += self.moves[self.dir][0]
                self.pos[1] += self.moves[self.dir][1]


        
    def getPos(self) -> List[int]:
        return self.pos

    def getDir(self) -> str:
        return self.dirMap[self.dir]
        

# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()