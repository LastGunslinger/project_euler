from loguru import logger

from project_euler.utilities import is_odd, is_prime, int_to_list, list_to_int


prompt = '''
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
'''


def is_permutation(x: int, y: int) -> bool:
    return sorted(int_to_list(x)) == sorted(int_to_list(y))


def sort_int(x: int):
    lst = sorted(int_to_list(x))
    return ''.join(str(x) for x in lst)


def solve():
    logger.debug(prompt)
    primes = []
    ignore = [1487, 4817, 8147]
    # ignore = []
    result_dict = {}
    num_range = (x for x in range(1000, 9999) if is_odd(x) and x not in ignore)
    for num in num_range:
        if not is_prime(num):
            continue
        primes.append(num)
        if result_dict.get(sort_int(num)):
            result_dict[sort_int(num)].append(num)
        else:
            result_dict[sort_int(num)] = [num]

    result_dict = {key: value for key, value in result_dict.items() if len(value) >= 3}
    for key, value in result_dict.items():
        last_diff = 0
        for i, val in enumerate(value):
            if i == 0:
                continue
            diff = val - value[i - 1]
            if diff == last_diff:
                logger.info({key: value[i - 2:i + 1]})
                return f'{value[i - 2]}{value[i - 1]}{value[i]}'
            else:
                last_diff = diff
