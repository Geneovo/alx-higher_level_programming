#!/usr/bin/Python3
"""Script that reads stdin line by line and computes matrics"""

import sys


def print_metrics(total_size, status_codes):
    """Prints metrics"""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes):
        print("{}: {}".format(code, status_codes[code]))


def main():
    """Main function to compute metrics"""
    total_size = 0
    status_codes = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0
    }
    count = 0

    try:
        for line in sys.stdin:
            count += 1
            parts = line.split()
            if len(parts) >= 7:
                total_size += int(parts[-1])
                sc = parts[-2]
                if sc in status_codes:
                    status_codes[sc] += 1

            if count % 10 == 0:
                print_metrics(total_size, status_codes)

    except KeyboardInterrupt:
        print_metrics(total_size, status_codes)
        raise
