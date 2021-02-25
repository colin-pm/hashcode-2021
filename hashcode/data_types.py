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
        self._queues = defaultdict(list)

    def add_input_street(self, street):
        self._input_streets.append(street)

    def select_street(self, street):
        self._active_street = street

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
