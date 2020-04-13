#! /usr/bin/env python
# author @ github.com/j-000
from collections import Counter


class Kaprekar:

    def __init__(self, n):
        self.starting_number = n
        self.seen = list()
        self.info = ''
        self.max_loop = 0
        self.run_loop(self.starting_number)

    def __str__(self):
        return self.info

    def run_loop(self, number, loop_number=0):
        if loop_number == 0:
            self.info += f'Started loop with {number}.\n'
        # If number has been seen or has only 1 unique digit, game over.
        if len(set(str(number))) == 1 or number in self.seen:
            # Store max loop
            self.max_loop = loop_number
        else:
            # Add number to seen set
            self.seen.append(number)
            # Perform algorithm
            a = int(''.join(sorted(str(number), reverse=True)))
            b = int(''.join(sorted(str(a))))
            c = a - b
            self.info += f'\t#{loop_number+1}) {a} - {b} = {c}\n'
            return self.run_loop(c, loop_number=loop_number + 1)