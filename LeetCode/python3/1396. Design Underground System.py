class UndergroundSystem:

    def __init__(self):
        self.check_ins = {}  # {id: (station_name, start_time)}
        self.average_travel_time = {}  # {(origin, destination): (time, cardinality))

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_ins[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        origin_station, start_time = self.check_ins.pop(id)

        average_time_info = self.average_travel_time.get((origin_station, stationName))
        if average_time_info is None:
            self.average_travel_time[(origin_station, stationName)] = (t - start_time, 1)
            return

        average_time, cardinality = average_time_info
        self.average_travel_time[(origin_station, stationName)] = (
            (average_time * cardinality + (t - start_time)) / (cardinality + 1),
            cardinality + 1
        )

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.average_travel_time[(startStation, endStation)][0]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)


if __name__ == "__main__":
    us = UndergroundSystem()
    us.checkIn(1, "a", 1)
    us.checkOut(1, "b", 2)
    print(us.average_travel_time)
    us.checkIn(2, "a", 3)
    us.checkOut(2, "b", 5)
    print(us.average_travel_time)
    print(us.getAverageTime("a", "b"))
