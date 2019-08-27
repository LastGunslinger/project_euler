from loguru import logger

from project_euler.utilities import primes, is_prime


prompt = '''
The prime 41, can be written as the sum of six consecutive primes:
41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
'''


def is_permutation(x: int, y: int) -> bool:
    return sorted(int_to_list(x)) == sorted(int_to_list(y))


def sort_int(x: int):
    lst = sorted(int_to_list(x))
    return ''.join(str(x) for x in lst)


def solve():
    sum_limit = 100
    logger.debug(prompt)

