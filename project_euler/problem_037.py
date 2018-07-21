'''
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

Note: 2, 3, 5, and 7 are not considered to be truncatable primes.
'''

import time
from .utilities import primes, is_prime
from termcolor import colored


def left_truncatable(number: int):
    num_str = str(number)
    if len(num_str) == 1:
        return is_prime(number)
    elif is_prime(number):
        return left_truncatable(int(num_str[1:]))
    else:
        return False


def right_truncatable(number: int):
    num_str = str(number)
    if len(num_str) == 1:
        return is_prime(number)
    elif is_prime(number):
        return right_truncatable(int(num_str[:-1]))
    else:
        return False


def truncatable_prime(number: int):
    return left_truncatable(number) and right_truncatable(number)


def main():
    result = set()
    for prime in primes(11):  # Start generating primes at 11 due to problem restrictions
        if truncatable_prime(prime):
            print(f'Truncatable prime: {prime}')
            result.add(prime)
            if len(result) == 11:
                print(sorted(result))
                return sum(result)


if __name__ == '__main__':
    start = time.time()
    print(f'Result: {colored(main(), "green")}')
    print('--- {} seconds ---'.format(time.time() - start))
