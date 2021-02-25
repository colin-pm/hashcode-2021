import argparse
from hashcode.simulation import Simulation
from hashcode.output import output


def main():
    parser = argparse.ArgumentParser(description='Generates hashcode solution')
    parser.add_argument('input')
    parser.add_argument('output')

    args = parser.parse_args()
    run(input_file=args.input, output_file=args.output)


def run(input_file, output_file):
    print(f"Input: {input_file}, Output: {output_file}")
    s = Simulation(input_file)

    # Crude pattern making
    patterns = {}
    duration = 2
    for intersection in s.intersections:
        patterns[intersection.intersection_number] = [(street.name, duration) for street in intersection.input_streets]
    s.run()
    output(output_file)
    return None
