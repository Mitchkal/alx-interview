#!/usr/bin/python3
"""
module log parsing
Process stdin line by line and
computes metrics
"""

import re
import signal
import sys


total_file_size = 0
line_count = 0
status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0,
                      405: 0, 500: 0}


def handle_signal(sig, frame):
    """
    handles the signals
    """
    print_statistics()
    sys.exit(0)


def print_statistics():
    """
    prints the total file size
    and the staus code counts
    """
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code] > 0:
            print(f"{code}: {status_code_counts[code]}")


signal.signal(signal.SIGINT, handle_signal)

par = (r'^(\d+\.\d+\.\d+\.\d+) - \[.*?\] "GET /projects/260 HTTP/1\.1" '
       r'(\d+) (\d+)')

log_pattern = re.compile(par)

try:
    for line in sys.stdin:
        line = line.strip()
        match = log_pattern.match(line)
        if match:
            status_code = int(match.group(2))
            file_size = int(match.group(3))

            if status_code in status_code_counts:
                total_file_size += file_size
                status_code_counts[status_code] += 1
                line_count += 1
                if line_count % 10 == 0:
                    print_statistics()
except KeyboardInterrupt:
    pass
print_statistics()
