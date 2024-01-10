#!/usr/bin/Python3
"""Script that reads stdin line by line and computes matrics"""


def print_metrics(total_size, status_codes):
    """Prints metrics"""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes):
        print("{}: {}".format(code, status_codes[code]))


if __name__ == "__main__":
    import sys

    total_size = 0
    status_codes = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    count = 0

    try:
        for line in sys.stdin:
            if count == 10:
                print_metrics(total_size, status_codes)
                count = 1
            else:
                count += 1

            line = line.split()

            try:
                total_size += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in valid_codes:
                    if status_codes.get(line[-2], -1) == -1:
                        status_codes[line[-2]] += 1
                    else:
                        status_codes[line[-2]] += 1
            except IndexError:
                pass

        print_metrics(total_size, status_codes)

    except KeyboardInterrupt:
        print_metrics(total_size, status_codes)
        raise
