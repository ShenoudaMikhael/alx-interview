#!/usr/bin/python3
import sys


total_size = 0
code = 0
counter = 0
dict_status_count = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0,
}


def print_ocur(dict_status_count, total_size):
    """print_ocur function"""
    print("File size: {}".format(total_size))
    for k, v in sorted(dict_status_count.items()):
        if v != 0:
            print("{}: {}".format(k, v))


try:
    for line in sys.stdin:
        strip_line = line.split()
        rev_line = strip_line[::-1]

        if len(rev_line) > 2:
            counter += 1

            if counter <= 10:
                total_size += int(rev_line[0])
                code = rev_line[1]

                if code in dict_status_count.keys():
                    dict_status_count[code] += 1

            if counter == 10:
                print_ocur(dict_status_count, total_size)
                counter = 0

finally:
    print_ocur(dict_status_count, total_size)
