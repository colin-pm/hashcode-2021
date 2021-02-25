from collections import defaultdict


class Intersection:
    def __init__(self, input_streets, output_streets):
        self._input_streets = input_streets
        self._active_street = None
        self._changed = False
        self._queues = defaultdict(list)

    def select_street(self, street):
        self._active_street = street
        self._changed = True

    def step(self):
        if self._changed:
            self._changed = False
        else:
            if len(self._queues[self._active_street.name]):
                next_car = self._queues.pop()
                next_street = next_car.streets.pop()
                next_street.add_car(next_car)

    def add_car(self, car, street):
        self._queues[street.name].append(car)

