#!/usr/bin/python3
"""Log parsing script for reads stdin and computes metrics."""
import sys
import re


def print_stats(total_size, status_counts):
    """Print current statistics."""
    print("File size: {}".format(total_size))
    for code in sorted(status_counts.keys()):
        print("{}: {}".format(code, status_counts[code]))


def main():
    """Main function to parse log lines from stdin."""
    total_size = 0
    status_counts = {}
    valid_codes = {'200', '301', '400', '401', '403', '404', '405', '500'}
    line_count = 0
    pattern = re.compile(
        r'^\d{1,3}(\.\d{1,3}){3} - \[.+\] "GET /projects/260 HTTP/1\.1" (\d+) (\d+)$'
    )

    try:
        for line in sys.stdin:
            line = line.strip()
            match = pattern.match(line)
            if not match:
                continue
            status_code = match.group(2)
            file_size = int(match.group(3))
            total_size += file_size
            if status_code in valid_codes:
                status_counts[status_code] = status_counts.get(
                    status_code, 0) + 1
            line_count += 1
            if line_count % 10 == 0:
                print_stats(total_size, status_counts)
    except KeyboardInterrupt:
        print_stats(total_size, status_counts)
        raise


if __name__ == "__main__":
    main()
