#!/usr/bin/python3
"""
Log parsing
"""


import sys

count = 0
total_file_size = 0
status_dict = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0,
               '404': 0, '405': 0, '500': 0}

try:
    for line in sys.stdin:
        line = line.rstrip()
        line_split = line.split(" ")

        if len(line_split) > 4:
            status_code = line_split[-2]
            file_size = int(line_split[-1])

        # look for status code in dict and increment it
        if status_code in status_dict.keys():
            status_dict[status_code] += 1

        count += 1
        # increase total file size
        total_file_size += file_size
        if count == 10:
            print('File size: {}'.format(total_file_size))
            for key, value in sorted(status_dict.items()):
                if value != 0:
                    print('{}: {}'.format(key, value))
            count = 0  # reset count

except Exception as err:
    pass

finally:
    print('File size: {}'.format(total_file_size))
    for key, value in sorted(status_dict.items()):
        if value != 0:
            print('{}: {}'.format(key, value))
