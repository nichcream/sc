#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser()

parser.add_argument('from_src', type=str,
                    help='source that comes after \'- from\' (typed in full)')
parser.add_argument('-f', '--file', type=str,
                    help='File or path leading to the referenced proprietary files list')
parser.add_argument('-o', '--out', type=str,
                    help='File or path leading to the output filtered proprietary files list')

args = parser.parse_args()

lines = [ line for line in open(args.file if args.file else 'proprietary-files-qc.txt', 'r') ]

canCopy = False

newlines= list()

for index, line in enumerate(lines):
    # Remove '\n'
    line = line[:-1]

    if len(line) == 0:
        if canCopy:
            newlines.append('')
        canCopy = False
        continue

    if (line.startswith('#')) and (' - from' in line):
        foo = line.split(' - from ')
        if foo[1] == args.from_src:
        	canCopy = True

    if canCopy:
        newlines.append(line)

with open(args.out if args.out else 'new.txt', 'w') as f:
    for line in newlines:
        f.write("%s\n" % line)

    f.close()
