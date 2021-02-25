import os
from collections import defaultdict

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

def camerons_second_solution(time, cars, streets, intersections, output_file):
    s_scores = defaultdict(int)

    for c in cars:
        for p in c.path:
            s_scores[p] += 1

    with open(output_file, 'w') as f:
        f.write(f'{len(intersections)}\n')
        for i in intersections:
            f.write(f'{i._intersection_number}\n')
            f.write(f'{len(i._input_streets)}\n')

            o = []
            for s in i._input_streets:
                if s_scores[s] != 0:
                    i.select_street(s)
                    o.append(f'{i._active_street.name} 1\n')
            f.write(f'{len(o)}')
            f.write(''.join(o))


for f in os.listdir('inputs'):
    print(f)
    input_thing = read_file(os.path.join('inputs', f))

    camerons_first_solution(input_thing['time'], input_thing['cars'], input_thing['streets'], input_thing['intersections'], os.path.join('outputs', f))
