from dataclasses import dataclass
from collections import defaultdict


@dataclass
class Street:
    name: str
    length: int
    start_intersection: int
    end_intersection: int


class Car:
    def __init__(self, path):
        self.time_on_road = 0
        self.distance = 0
        self.path = path
        self.street_remaining = len(path[0])
        
    def step(self):
        
        # if car is done
        if len(self.path) == 0:
            return

        self.time_on_road += 1

        if self.street_remaining == 0:
            # car is in the intersection
            print(self.path[0])
            intersection = self.path[0].end_intersection
            # if we move through the intersection...
            if intersection.pass_car(self):
                # remove the path
                self.path.pop(0)
                # reset street_remaining for the new current street
                self.street_remaining = self.path[0].length
            
        else:
            # move down the street one unit
            self.street_remaining -= 1


class Intersection:
    def __init__(self, intersection_number):
        self.intersection_number = intersection_number
        self.input_streets = []
        self._active_street = None
        self._counter = 0
        self._pattern = None
        self._queues = defaultdict(list)

    def add_input_street(self, street):
        self.input_streets.append(street)

    def update_light(self):
        self._active_street = self._pattern.update()

    def add_pattern(self, pattern):
        """
        :param pattern: List of tuples in order as (street, duration)
        :return:
        """
        self._pattern = self.Pattern(pattern)

    def pass_car(self, car, street):

        #skip if this street is not active
        if self._active_street != street:
            return False

        # skip if car is not next in the queue
        if self._queues[street.name][0] != car:
            return False

        # remove the car from the queue
        self._queues[street.name].pop(0)
        
        #indicate that the car has left the intersection
        return True

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
                for _ in range(pattern_item[1]):
                    self._pattern.append(pattern_item[0])

        def update(self):
            if self._pattern:
                street = self._pattern[self._counter % len(self._pattern)]
                self._counter += 1
                return street
