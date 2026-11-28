class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.map = {}
        self.map[1] = big
        self.map[2] = medium
        self.map[3] = small

    def addCar(self, carType: int) -> bool:
        if self.map[carType] > 0: 
            self.map[carType] -= 1
            return True
        else:
            return False
