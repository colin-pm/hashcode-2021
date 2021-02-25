from .data_types import Street, Car, Intersection


def read_file(file_path):
    with open(file_path, 'r') as f:
        time, number_of_intersections, number_of_streets, number_of_cars, score = f.readline().split(' ')

        streets = []
        cars = []
        intersections = []

        for i in range(int(number_of_intersections)):
            intersections.append(Intersection(i))

        for _ in range(int(number_of_streets)):
            l = f.readline().split(' ')
            street = Street(l[2], int(l[3]), int(l[0]), int(l[1]))
            streets.append(street)
            intersections[int(l[1])].add_input_street(street)

        for _ in range(int(number_of_cars)):
            l = f.readline().split(' ')
            p = int(l[0])
            car = Car([])
            for i in range(1, len(l)):
                car.path.append(l[i])
            cars.append(car)

        return {'streets': streets, 'cars': cars, 'score': score, 'intersections': intersections}