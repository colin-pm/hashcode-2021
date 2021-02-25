import os

from .data_types import Street, Car
from .input import read_file

def camerons_first_solution(time, cars, streets, intersections, output_file):
    with open(output_file, 'w') as f:
        f.write(f'{len(intersections)}\n')
        for i in intersections:
            f.write(f'{i._intersection_number}\n')
            f.write(f'{len(i._input_streets)}\n')
            for s in i._input_streets:
                i.select_street(s)
                f.write(f'{i._active_street.name} 1\n')




for f in os.listdir('inputs'):
    print(f)
    input_thing = read_file(os.path.join('inputs', f))

    camerons_first_solution(input_thing['time'], input_thing['cars'], input_thing['streets'], input_thing['intersections'], os.path.join('outputs', f))
