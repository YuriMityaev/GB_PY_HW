class Road:
    def __init__(self, lh, wh):
        self._lh = lh
        self._wh = wh

    def for_road(self, weight=25, ths=5):
        return f"{self._lh} m * {self._wh} m * {weight} кг * {ths} см =" \
               f"{(self._lh * self._wh * weight * ths) / 1000} т"


road_1 = Road(15365, 10)
print(road_1.for_road(25, 6))
