#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser()

parser.add_argument('src_name', type=str,
                    help='source name that comes after \'- from\' (typed in full)')
parser.add_argument('-f', '--file', type=str,
                    help='File or path leading to the referenced proprietary files list')
parser.add_argument('-o', '--out', type=str,
                    help='File or path leading to the output filtered proprietary files list')

args = parser.parse_args()

lines = [ line for line in open(args.file if args.file else 'proprietary-files-qc.txt', 'r') ]

canCopy = False

newlines= list()

for line in lines:
    # Remove '\n'
    if line[-1:] == '\n':
        line = line[:-1]

    # end of section
    if len(line) == 0:
        if canCopy:
            newlines.append('')
        canCopy = False
        continue

    if (line.startswith('#')) and (' - from' in line):
        foo = line.split(' - from ')
        if foo[1] == args.src_name:
            canCopy = True

    if canCopy:
        newlines.append(line)

with open(args.out if args.out else 'new.txt', 'w') as f:
    for index, line in enumerate(newlines):
        # if last line is empty, ignore
        if (index < len(newlines) - 1) or (len(line) > 0):
            f.write("%s\n" % line)
