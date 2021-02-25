from hashcode.input import read_file


class Simulation:
    def __init__(self, input_file):
        data = read_file(input_file)
        self._duration = data['time']
        self._streets = data['streets']
        self._cars = data['cars']
        self._score = data['score']
        self._intersections = data['intersections']