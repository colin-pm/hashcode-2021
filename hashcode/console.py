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
    duration = 3
    for intersection in s.intersections:
        pattern = [(street.name, duration) for street in intersection.input_streets]
        patterns[intersection.intersection_number] = pattern
        intersection.add_pattern(pattern)
    s.run()
    output(patterns, output_file)
    return None


if __name__ == '__main__':
    main()
