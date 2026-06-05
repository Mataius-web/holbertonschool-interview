#!/usr/bin/python3
"""Reads stdin line by line and computes metrics."""
import sys


def print_stats(total_size, status_counts):
    """Print the accumulated file size and status code counts."""
    print("File size: {}".format(total_size))
    for code in sorted(status_counts):
        if status_counts[code] > 0:
            print("{}: {}".format(code, status_counts[code]))


if __name__ == "__main__":
    total_size = 0
    line_count = 0
    status_counts = {200: 0, 301: 0, 400: 0, 401: 0,
                     403: 0, 404: 0, 405: 0, 500: 0}

    try:
        for line in sys.stdin:
            parts = line.split()
            if len(parts) < 2:
                continue

            try:
                size = int(parts[-1])
            except ValueError:
                continue

            try:
                status = int(parts[-2])
                if status in status_counts:
                    status_counts[status] += 1
            except ValueError:
                pass

            total_size += size
            line_count += 1

            if line_count % 10 == 0:
                print_stats(total_size, status_counts)
    except KeyboardInterrupt:
        print_stats(total_size, status_counts)
        raise

    print_stats(total_size, status_counts)
