#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser(description='Create indents for a range of lines')

parser.add_argument('file_name',
                    help='File to indent')
parser.add_argument('start_line', type=int,
                    help='line number to start indenting')
parser.add_argument('end_line', type=int,
                    help='line number to stop indenting')
parser.add_argument('-s', '--indent-spaces', type=int,
                    help='indent with')
parser.add_argument('-i', '--ignore-undent', action='store_true',
                    help='Only indent lines which have already an indent')

args = parser.parse_args()

lines = [ line for line in open(args.file_name, 'r') ]

for i in range(args.start_line - 1, args.end_line):

    indent = args.indent_spaces * ' ' if args.indent_spaces else 4 * ' '

    if not args.ignore_undent or (args.ignore_undent and lines[i].strip()):
        lines[i] = indent + lines[i]

with open(args.file_name, 'w') as file:
    for line in lines:
        file.write(line)

    file.close()
