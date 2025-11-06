"""log_parser.py - simple placeholder
"""

import sys

def parse_log(path):
    """Placeholder log parser"""
    print(f"Parsing {path}")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        parse_log(sys.argv[1])
    else:
        print('Usage: python log_parser.py <logfile>')
