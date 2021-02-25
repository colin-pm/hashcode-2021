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
        self.distance = 0
        self.path = path
        self.street_remaining = path[0].length
        
    def step(self):
        
        # if car is done
        if(len(path) == 0)
            return

        if(self.street_remaining == 0):
            # car is in the intersection
            intersection = path[0].end_intersection
            # if we move through the intersection...
            if(intersection.pass_car(self)):
                # remove the path
                self.path.pop(0)
                # reset street_remaining for the new current street
                self.street_remaining = path[0].length
            
        else:
            # move down the street one unit
            self.street_remaining--
            

    


class Intersection:
    def __init__(self, intersection_number):
        self._intersection_number = intersection_number
        self._input_streets = []
        self._active_street = None
        self._counter = 0
        self._pattern = None
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

    def pass_car(self, car, street):

        #skip if this street is not active
        if(_active_street != street):
            return false

        # skip if car is not next in the queue
        if(self._queues[street.name][0] != car)
           return false

        # remove the car from the queue
        self._queues[street.name].pop(0)
        
        #indicate that the car has left the intersection
        return true

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
