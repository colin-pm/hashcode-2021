def output(intersection_patterns, output_file):
    """

    :param intersection_patterns: Dict where intersection number is key and each item is a list of tuples of street name and duration
    :param output_file: File to write output to
    :return:
    """
    with open(output_file, 'w') as f:
        f.write(f'{len(intersection_patterns)}\n')
        for intersection, pattern in intersection_patterns.items():
            f.write(f'{intersection}\n')
            f.write(f'{len(pattern)}\n')
            for street, duration in pattern:
                f.write(f'{street} {duration}')
