import argparse


def main():
    parser = argparse.ArgumentParser(description='Generates hashcode solution')
    parser.add_argument('input')
    parser.add_argument('output')

    args = parser.parse_args()
    run(input_file=args.input, output_file=args.output)


def run(input_file, output_file):
    print(f"Input: {input_file}, Output: {output_file}")
    # TODO Insert entry point
    return None
