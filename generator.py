#!/usr/bin/env python
# coding : utf-8

import argparse
import itertools


def main():
    parser = argparse.ArgumentParser(description='Generates .hcmasks file')
    parser.add_argument('-m', '--min', required=True, type=int, help='Password minimum size')
    parser.add_argument('-M', '--max', required=True, type=int, help='Password maximum size')
    parser.add_argument('-t', '--toggle', action='store_true', help='Toggle case')
    parser.add_argument('-s', '--special', action='store_true', help='Add ending special character')

    args = parser.parse_args()

    if args.min > args.max:
        parser.print_help()
        exit(1)

    accumulator = 1
    while True:
        charset = '?l?u,'
        word = '?u'
        if args.toggle:
            word = '?u'+'?1'*accumulator
        else:
            word = '?u'+'?l'*accumulator
        digit = '?d'
        if args.special:
            special = '?s'
        else:
            special = ''
        for number_digit in range(1, 5):
            mask = [word, digit*number_digit, special]
            size_mask = len(''.join(mask))/2
            if size_mask > args.max:
                exit(0)
            if args.min <= size_mask <= args.max:
                for elem in itertools.permutations(mask):
                    print(charset+''.join(elem))
        accumulator += 1


if __name__ == "__main__":
    # execute only if run as a script
    main()
