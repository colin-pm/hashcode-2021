from .data_types import Street, Car, Intersection


def read_file(file_path):
    with open(file_path, 'r') as f:
        time, number_of_intersections, number_of_streets, number_of_cars, score = [int(val) for val in f.readline().split(' ')]

        streets = {}
        cars = []
        intersections = []

        for i in range(number_of_intersections):
            intersections.append(Intersection(i))

        for _ in range(number_of_streets):
            l = f.readline().split(' ')
            street = Street(l[2], int(l[3]), int(l[0]), int(l[1]))
            streets[street.name] = (street)
            intersections[int(l[1])].add_input_street(street)

        for _ in range(number_of_cars):
            l = f.readline().split(' ')
            p = int(l[0])
            car = Car([])
            for i in range(1, len(l)):
                car.path.append(l[i])
                i = intersections[streets[car.path[0]].end_intersection]
                i.add_car(car, streets[car.path[0]])

            cars.append(car)

        return {'time': time, 'streets': streets, 'cars': cars, 'score': score, 'intersections': intersections}
