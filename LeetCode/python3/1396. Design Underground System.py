from collections import defaultdict


class UndergroundSystem:

    def __init__(self):
        self.check_ins = {}  # {id: (station_name, start_time)}
        self.travel_times = defaultdict(lambda: (0, 0))  # {(origin, destination): (total_time, count))

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_ins[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        origin_station, start_time = self.check_ins.pop(id)
        total_time, count = self.travel_times[(origin_station, stationName)]
        self.travel_times[(origin_station, stationName)] = (total_time + t - start_time, count + 1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total_time, count = self.travel_times[(startStation, endStation)]
        return total_time / count


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)


if __name__ == "__main__":
    us = UndergroundSystem()
    us.checkIn(1, "a", 1)
    us.checkOut(1, "b", 2)
    print(us.travel_times)
    us.checkIn(2, "a", 3)
    us.checkOut(2, "b", 5)
    print(us.travel_times)
    print(us.getAverageTime("a", "b"))
