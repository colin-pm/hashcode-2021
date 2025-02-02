from hashcode.input import read_file


class Simulation:
    def __init__(self, input_file):
        data = read_file(input_file)
        self.duration = data['time']
        self.streets = data['streets']
        self.cars = data['cars']
        self.score = data['score']
        self.intersections = data['intersections']
        self.patterns = {}

    def run(self):
        for _ in range(self.duration):
            for intersection in self.intersections:
                intersection.update_light()
            for car in self.cars:
                car.step()
