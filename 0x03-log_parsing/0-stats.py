#!/usr/bin/python3
"""
    a script that reads stdin line by line and computes metrics:
    input format: <IP Address> - [<date>]
    "GET /projects/260 HTTP/1.1" <status code> <file size>
"""
import sys


def print_stats(total_size, status_codes):
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


def parse_line(line):
    parts = line.split()
    if len(parts) >= 7:
        ip = parts[0]
        status_code = parts[-2]
        file_size = parts[-1]
        return ip, status_code, file_size
    return None, None, None


def main():
    total_size = 0
    status_codes = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0
    }

    try:
        line_count = 0
        for line in sys.stdin:
            line_count += 1
            ip, status_code, file_size = parse_line(line)
            if ip and status_code and file_size:
                total_size += int(file_size)
                if status_code in status_codes:
                    status_codes[status_code] += 1

            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise


if __name__ == "__main__":
    main()
