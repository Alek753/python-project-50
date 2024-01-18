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
        default='stylish',
        choices=['stylish', 'plain', 'json'],
        help='set format of output'
    )
    args = parser.parse_args()
    fo = open('out.txt', 'w')
    fo.write(generate_diff(args.first_file,
                           args.second_file,
                           formatter=args.format))
    fo.close()


if __name__ == '__main__':
    main()
