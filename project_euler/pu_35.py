'''
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?

'''

import time
from termcolor import colored

import itertools
from .primes import gen_primes, is_prime
from typing import Set


def rotations(number: int) -> Set[int]:
    num_str = str(number)
    for index in range(len(num_str)):
        if index == 0:
            yield number
        else:
            yield int(num_str[index:] + num_str[:index])


def main():
    # Prefill set with known circular primes
    result = {2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97}
    for prime in gen_primes(max(result) + 1, 1000000):
        if prime in result:
            continue
        print(f'Prime: {prime}')
        for rotation in rotations(prime):
            if not is_prime(rotation):
                break
        else:
            [result.add(x) for x in rotations(prime)]
    print(sorted(result))
    return len(result)


if __name__ == '__main__':
    start = time.time()
    print(f'Result: {colored(main(), "green")}')
    print('--- {} seconds ---'.format(time.time() - start))
