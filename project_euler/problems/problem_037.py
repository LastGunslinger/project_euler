prompt = '''

The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

Note: 2, 3, 5, and 7 are not considered to be truncatable primes.
'''
from ..utilities import primes
import typing as typ


prime_set = set()


def left_truncatable(number: int):
    if len(str(number)) == 1:
        return number in prime_set
    elif number in prime_set:
        return left_truncatable(int(str(number)[1:]))
    else:
        return False


def right_truncatable(number: int):
    if len(str(number)) == 1:
        return number in prime_set
    elif number in prime_set:
        return right_truncatable(int(str(number)[:-1]))
    else:
        return False


def solve(logger):
    logger.debug(prompt)
    result = set()
    prime_set.update(primes(1000000))
    for prime in prime_set:
        if prime <= 7:
            continue
        if left_truncatable(prime) and right_truncatable(prime):
            logger.debug(f'Truncatable prime: {prime}')
            result.add(prime)
        if len(result) == 11:
            return sum(result)
