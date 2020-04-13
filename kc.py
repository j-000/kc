#! /usr/bin/env python
# author @ github.com/j-000
from tqdm import tqdm
from kaprekar import Kaprekar
from collections import Counter
from prettytable import PrettyTable
import argparse


def main(_min, _max):
    data_table = PrettyTable(field_names=['Loop count', 'Frequency', '%'])
    kc_objects = []
    print(f'\nStarting with range ({_min}, {_max}) of {_max - _min} iterations.')
    # Loop through each number in the range
    for number in tqdm(range(_min, _max)):
        # Initialise Kaprekar
        k = Kaprekar(number)
        # Store object in list
        kc_objects.append(k)
    # Calculate max loop frequency for range
    max_loops_counter = Counter([kc.max_loop for kc in kc_objects])
    # # Sort dict by loop count and print
    sorted_max_loops_dict = dict(sorted(max_loops_counter.items(),
                                        key=lambda x: x[0]))
    for (a, b) in sorted_max_loops_dict.items():
        c = round((b / (_max - _min) * 100), 2)
        data_table.add_row([a, b, c])
    print(data_table)

    most_seen_numbers = Counter([i for kc in kc_objects for i in kc.seen])
    most_common_seen = most_seen_numbers.most_common(1)[0]
    most_common_seen_percentage = round(
        (most_common_seen[1] / (_max - _min)) * 100, 2)
    print(f'For the range ({_min}, {_max}), out of {_max - _min} iterations, '
          f'the number {most_common_seen[0]} appears {most_common_seen[1]} '
          f'times or {most_common_seen_percentage}% of the time.')

    kc_most_seen = Kaprekar(most_common_seen[0])
    print(f'The most common number ({most_common_seen[0]}), finishes in '
          f'{kc_most_seen.max_loop} loop(s).')


if __name__ == '__main__':
    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', help='One single integer, a range or multiple.',
                        nargs='+', type=int, required=True)
    parser.add_argument('-wf', help='Write results to file.',
                        required=False, action='store_true')
    parser.add_argument('-pi', help='Print info.', action='store_false')
    args = parser.parse_args()

    if len(args.i) == 2 and (args.i[0] < args.i[1]):
        main(*args.i)
    else:
        for n in args.i:
            k = Kaprekar(n)
            if args.pi:
                print(k)
