import os
from collections import defaultdict, Counter
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
        # f.write(f'{len(intersections)}\n')
        i_counter = 0
        output_list = []
        for i in intersections:
            # f.write(f'{i._intersection_number}\n')

            o = []
            intersection_scores = Counter({k.name:s_scores[k.name] for k in i._input_streets})
            # total_i_scores = sum(intersection_scores)
            # avg_scores = total_i_scores / len(intersection_scores)
            for s in i._input_streets:
                if s_scores[s.name] != 0:
                    l = 2

                    if s.name == intersection_scores.most_common(1)[0][0]:
                        l = 3 #round(l * intersection_scores.most_common(1)[0][1] / avg_scores, 0)
                    i.select_street(s)
                    o.append(f'{i._active_street.name} {l}\n')
            if len(o) > 0:
                output_list.append(f'{i._intersection_number}\n')
                output_list.append(f'{len(o)}\n')
                output_list.append(''.join(o))
                i_counter += 1
        output_list.insert(0, f'{i_counter}\n')
        f.write(''.join(output_list))

def camerons_third_solution(time, cars, streets, intersections, output_file):
    s_scores = defaultdict(int)

    for c in cars:
        for p in c.path:
            s_scores[p] += 1

    with open(output_file, 'w') as f:
        # f.write(f'{len(intersections)}\n')
        i_counter = 0
        output_list = []
        for i in intersections:

            o = []
            for s in i._input_streets:
                if s_scores[s.name] != 0:
                    i.select_street(s)
                    o.append(f'{i._active_street.name} {l}\n')
            if len(o) > 0:
                output_list.append(f'{i._intersection_number}\n')
                output_list.append(f'{len(o)}\n')
                output_list.append(''.join(o))
                i_counter += 1
        output_list.insert(0, f'{i_counter}\n')
        f.write(''.join(output_list))

for f in os.listdir('inputs'):
    print(f)
    input_thing = read_file(os.path.join('inputs', f))

    camerons_second_solution(input_thing['time'], input_thing['cars'], input_thing['streets'], input_thing['intersections'], os.path.join('outputs', f))
