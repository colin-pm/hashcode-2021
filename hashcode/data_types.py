from dataclasses import dataclass
from collections import defaultdict


@dataclass
class Street:
    name: str
    length: int
    start_intersection: int
    end_intersection: int


@dataclass
class Car:
    path: list


class Intersection:
    def __init__(self, intersection_number):
        self._intersection_number = intersection_number
        self._input_streets = []
        self._active_street = None
        self._counter = 0
        self._pattern = None
        self._changed = False
        self._queues = defaultdict(list)

    def add_input_street(self, street):
        self._input_streets.append(street)

    def update_light(self):
        self._active_street = self._pattern.update()

    def add_pattern(self, pattern):
        """
        :param pattern: List of tuples in order as (street, duration)
        :return:
        """
        self._pattern = self.Pattern(pattern)

    def step(self):
        if self._changed:
            self._changed = False
        else:
            if len(self._queues[self._active_street.name]):
                next_car = self._queues[self._active_street.name].pop()
                next_street = next_car.path.pop()
                next_street.add_car(next_car)

    def add_car(self, car, street):
        self._queues[street.name].append(car)

    class Pattern:
        def __init__(self, pattern_list):
            """
            :param pattern_list: List of tuples in order as (street, duration)
            """
            self._pattern = []
            self._counter = 0
            for pattern_item in pattern_list:
                for _ in pattern_item[1]:
                    self._pattern.append(pattern_item[0])

        def update(self):
            street = self._pattern[self._counter % len(self._pattern)]
            self._counter += 1
            return street
