class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.parking_spaces = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        parking_index = carType - 1

        if self.parking_spaces[parking_index] == 0:
            return False

        self.parking_spaces[parking_index] -= 1
        return True


ps = ParkingSystem(1, 1, 0)
print(ps.addCar(1))
print(ps.addCar(2))
print(ps.addCar(3))
print(ps.addCar(1))
