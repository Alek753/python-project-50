#!/usr/bin/env python3
import argparse
from gendiff.generate_diff import generate_diff


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files an shows a difference.'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f',
        '--format',
        help='set format of output'
    )
    args = parser.parse_args()
#    print(generate_diff(args.first_file, args.second_file))
    fo = open('out.txt', 'w')
    fo.write(generate_diff(args.first_file, args.second_file))
    fo.close()


if __name__ == '__main__':
    main()
