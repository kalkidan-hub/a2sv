class UndergroundSystem:

    def __init__(self):
        self.startStations = {}
        self.journeyStatus = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.startStations[id] = (stationName,t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        s1,t1 = self.startStations[id]
        self.journeyStatus[(s1,stationName)].append(t-t1)
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        journey = self.journeyStatus[(startStation,endStation)]
        return sum(journey)/len(journey)


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)