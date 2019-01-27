class ElectricCar:

    def __init__(self, max_range):
        self.max_range = max_range
        self._traveled_distance = 0

    def drive(self, distance):
        if self._traveled_distance + distance > self.max_range:
            to_travel = self.max_range - self._traveled_distance
            self._traveled_distance = self.max_range
            return to_travel
        else:
            self._traveled_distance += distance
            return distance

    def charge(self):
        self._traveled_distance = 0


def test_electric_car_initialization():
    car = ElectricCar(100)  # ustawiam max_range
    assert car.max_range == 100


def test_electric_car_drive():
    car = ElectricCar(100)
    assert car.drive(50) == 50
    assert car.drive(50) == 50
    assert car.drive(50) == 0


def test_electric_car_drive_over_max_range_in_one_aproach():
    car = ElectricCar(100)
    assert car.drive(130) == 100


def test_electric_car_charge():
    car = ElectricCar(100)
    assert car.drive(100) == 100
    assert car.drive(1) == 0
    car.charge()
    assert car.drive(1) == 1