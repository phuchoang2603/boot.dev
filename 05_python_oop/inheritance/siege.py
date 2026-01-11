class Siege:
    def __init__(self, max_speed, efficiency):
        self.max_speed = max_speed
        self.efficiency = efficiency

    def get_trip_cost(self, distance, food_price):
        return distance / self.efficiency * food_price

    def get_cargo_volume(self):
        pass


class BatteringRam(Siege):
    def __init__(
        self,
        max_speed,
        efficiency,
        load_weight,
        bed_area,
    ):
        super().__init__(max_speed, efficiency)
        self.__load_weight = load_weight
        self.__bed_area = bed_area

    def get_trip_cost(self, distance, food_price):
        init_cost = super().get_trip_cost(distance, food_price)
        return init_cost + (self.__load_weight * 0.01)

    def get_cargo_volume(self):
        return self.__bed_area * 2


class Catapult(Siege):
    def __init__(self, max_speed, efficiency, cargo_volume):
        super().__init__(max_speed, efficiency)
        self.__cargo_volume = cargo_volume

    def get_cargo_volume(self):
        return self.__cargo_volume
