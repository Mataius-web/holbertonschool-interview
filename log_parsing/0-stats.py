#!/usr/bin/python3
"""script that reads stdin and computes metrics"""
import sys

if __name__ == "__main__":
    total_size = 0
    count = 0
    codes = {}
    valid_codes = [200, 301, 400, 401, 403, 404, 405, 500]

    try:
        for line in sys.stdin:
            try:
                parts = line.split()
                # check if the line has enough parts
                if len(parts) < 7:
                    continue
                # get the status code and file size
                status_code = parts[-2]
                file_size = parts[-1]
                # try to convert them to integers
                file_size = int(file_size)
                status_code = int(status_code)
                total_size = total_size + file_size
                if status_code in valid_codes:
                    if status_code not in codes:
                        codes[status_code] = 0
                    codes[status_code] = codes[status_code] + 1
                count = count + 1
            except Exception:
                continue

            if count % 10 == 0:
                print("File size: {}".format(total_size))
                for code in sorted(codes.keys()):
                    print("{}: {}".format(code, codes[code]))

    except KeyboardInterrupt:
        pass

    finally:
        print("File size: {}".format(total_size))
        for code in sorted(codes.keys()):
            print("{}: {}".format(code, codes[code]))
