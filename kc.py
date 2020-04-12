#! /usr/bin/env python
# author @ github.com/j-000
import json
from collections import Counter
import sys
import tqdm


seen = set()
seen_freq = dict()
all_seen_sets = list()


def kaprekar_constant(n, loop=0):
    if len(set(str(n))) == 1 or n in seen:
        # print(f'\tEnded with {loop} loops.')
        for p in seen:
            if str(p) in seen_freq:
                seen_freq[str(p)] += 1
            else:
                seen_freq[str(p)] = 1
        all_seen_sets.append(list(seen))
        seen.clear()
        return loop
    else:
        seen.add(n)
        a = int(''.join(sorted(str(n), reverse=True)))
        b = int(''.join(sorted(str(a))))
        c = a - b
        # print(f'\t{a} - {b} = {c}')
        return kaprekar_constant(c, loop=loop+1)


def main(_min, _max):
    loop_freq = dict()

    for i in tqdm.tqdm(range(_min, _max)):
        r = kaprekar_constant(i)
        if r in loop_freq:
            loop_freq[r] += 1
        else:
            loop_freq.update({r: 1})

    sorted_loop_freq = dict(sorted(loop_freq.items(), key=lambda x: x[0]))
    print(json.dumps(sorted_loop_freq, indent=4))

    frequency_counter = Counter([i for x in all_seen_sets for i in x])
    first_most_common = frequency_counter.most_common(1)[0]
    first_most_common_perc = round(
        ((first_most_common[1] / (_max - _min)) * 100), 2)
    print(f'The most common digit is {first_most_common[0]} at '
          f'{first_most_common[1]}/{_max - _min} or '
          f'{first_most_common_perc}%.')


if __name__ == '__main__':
    _min, _max = sys.argv[1:3]
    main(_min=int(_min), _max=int(_max))

