from .data_types import Street, Car

def read_file(file_path):
    with open(file_path, 'r') as f:
        time, number_of_intersections, number_of_streets, number_of_cars, score = f.readline().split(' ')

        streets = []
        cars = []
        for _ in range(int(number_of_streets)):
            l = f.readline().split(' ')
            streets.append(Street(l[2], int(l[3]), int(l[0]), int(l[1])))

        for _ in range(int(number_of_cars)):
            l = f.readline().split(' ')
            p = int(l[0])
            car = Car([])
            for i in range(1,len(l)):
                car.path.append(l[i])
            cars.append(car)
            
        return {'streets': streets, 'cars': cars, 'score': score}