#! /usr/bin/env python
# author @ github.com/j-000
import json
from collections import Counter
import tqdm
import argparse


seen = set()
seen_freq = dict()
all_seen_sets = list()


def kaprekar_constant(n, loop=0):
    # If the number contains at most 1 unique digit or it has been seen
    # then it is game over.
    if len(set(str(n))) == 1 or n in seen:
        # Update the resulting numbers frequency
        for p in seen:
            if str(p) in seen_freq:
                seen_freq[str(p)] += 1
            else:
                seen_freq[str(p)] = 1
        # Retain information of the seen set
        all_seen_sets.append(list(seen))
        # Clear the seen set
        seen.clear()
        return loop
    else:
        # Add number to seen set
        seen.add(n)
        # Perform algorithm
        a = int(''.join(sorted(str(n), reverse=True)))
        b = int(''.join(sorted(str(a))))
        c = a - b
        # Return next result / continue loop
        return kaprekar_constant(c, loop=loop+1)


def main(_min, _max):
    # This dictionary keeps track of the loop frequency
    loop_freq = dict()

    # Loop through each number in the range
    for i in tqdm.tqdm(range(_min, _max)):
        # Get loop count for i
        loop_count = kaprekar_constant(i)
        # Update loop count frequency
        if loop_count in loop_freq:
            loop_freq[loop_count] += 1
        else:
            loop_freq.update({loop_count: 1})
    # Sort loop frequency dictionary
    sorted_loop_freq = dict(sorted(loop_freq.items(), key=lambda x: x[0]))
    print('Loop distribution:')
    print(json.dumps(sorted_loop_freq, indent=4))
    # Create a frequency counter of all the numbers in all_seen_sets
    frequency_counter = Counter([i for x in all_seen_sets for i in x])
    # Get the most common number
    first_most_common = frequency_counter.most_common(1)[0]
    # Get the loop count for the most common number
    most_common_loop_count = kaprekar_constant(first_most_common[0])
    # Get the most common number's percentage
    first_most_common_perc = round(
        ((first_most_common[1] / (_max - _min)) * 100), 2)
    result_string = f'For all {_max} function calls for the range ' \
                    f'({_min}, {_max}), the digit {first_most_common[0]}'\
                    f' appears {first_most_common[1]} times or ' \
                    f'{first_most_common_perc}% of the time. ' \
                    f'This number ({first_most_common[0]}) terminates in ' \
                    f'{most_common_loop_count} loop(s).'
    print(result_string)
    return sorted_loop_freq, result_string


if __name__ == '__main__':
    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', help='One single integer, a range or multiple.',
                        nargs='+', type=int, required=True)
    parser.add_argument('-wf', help='Write results to file.',
                        required=False, action='store_true')
    args = parser.parse_args()
    # File data
    file_data = []

    # If an ordered range is provided (min, max),
    # output the loop distribution and the most common digit based.
    if len(args.i) == 2 and (args.i[0] < args.i[1]):
        freq_loop, result_str = main(*args.i)
        file_data += [freq_loop, result_str]
    # otherwise ran then individually.
    else:
        for number in args.i:
            kaprekar_constant(number)
    if args.wf and file_data:
        # Write file
        with open('data.txt', 'a+', encoding='utf-8') as file:
            for data in file_data:
                if type(data) is dict:
                    file.write(str(json.dumps(data, indent=4)) + '\n')
                else:
                    file.write(str(data) + '\n')
