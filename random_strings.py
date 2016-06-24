#!/usr/bin/env python
"""
Script to generate random DNA strings of a given length, for
testing purposes

TODO:
    - add option to provide desired GC-content for DNA
"""
import random
import string
import argparse

DNA = 1
RNA = 2
PROTEIN = 3
ALPHA = 4
ALPHANUMERIC = 5

def choose_base_list(list_choice):
    return {
        DNA: ['A', 'T', 'G', 'C'],
        RNA: ['A', 'U', 'G', 'C'],
        PROTEIN: [c for c in string.ascii_uppercase
                  if c not in ['B', 'J', 'O', 'U', 'X', 'Z']],
        ALPHA: string.ascii_uppercase,
        ALPHANUMERIC: string.ascii_uppercase + string.digits
    }[list_choice]

def generate_random_string(length, base_list):
    return ''.join(random.choice(base_list) for _ in xrange(length))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--number", nargs="?", default=1,
                        help="Number of strings to generate")
    parser.add_argument("-l", "--length", nargs="?", default=10,
                        help="Length of the desired string")
    parser.add_argument("-t", "--string_type", nargs="?", default=1,
                        help="1 for DNA, 2 for RNA, 3 for protein,\
                              4 for alphabet or 5 for alphanumeric. Defaults\
                              to DNA")
    parser.add_argument("-f", "--fasta_file", action="store_true",
                        help="Output the random strings as a FASTA-formatted\
                              file (with randomly generated labels)")

    opts = parser.parse_args()
    base_list = choose_base_list(int(opts.string_type))

    if opts.fasta_file:
        for idx in xrange(int(opts.number)):
            print '>entry_{}'.format(idx)
            print generate_random_string(int(opts.length), base_list)
    else:
        print '\n'.join(generate_random_string(int(opts.length), base_list)
                        for _ in xrange(int(opts.number)))

if __name__ == '__main__':
    main()

