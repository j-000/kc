#! /usr/bin/env python
# author @ github.com/j-000
import json
from collections import Counter
import tqdm


seen = set()
seenfreq = dict()


master = list()


def kc(n, loop=0):
    # if loop == 0:
    #     print(f'Starting with {n}')
    # if the number is 6174 or if the number contains only 1 digit
    # then it is game over
    if len(set(str(n))) == 1 or n in seen:
        # print(f'\tEnded with {loop} loops.')
        for p in seen:
            if str(p) in seenfreq:
                seenfreq[str(p)] += 1
            else:
                seenfreq[str(p)] = 1

        master.append(list(seen))
        seen.clear()
        return loop
    else:
        seen.add(n)
        a = int(''.join(sorted(str(n), reverse=True)))
        b = int(''.join(sorted(str(a))))
        c = a - b
        # print(f'\t{a} - {b} = {c}')
        return kc(c, loop=loop+1)


freq = dict()

if __name__ == '__main__':
    _min = 1111111
    _max = 10000000

    for i in range(_min, _max):
        r = kc(i)
        if r in freq:
            freq[r] += 1
            # freq[r]['%'] = round((freq[r]['max'] / (_max - _min)) * 100, 2)
        else:
            freq.update({r: 1})

    print(json.dumps(dict(sorted(freq.items(), key=lambda x: x[0])), indent=4))

    frequency_counter = Counter([i for x in master for i in x])
    first_most_common = frequency_counter.most_common(1)[0]

    print(f'The most common digit is {first_most_common[0]} at '
          f'{first_most_common[1]}/{_max-_min} or '
          f'{round(((first_most_common[1]/(_max-_min))*100),2)}%.')
