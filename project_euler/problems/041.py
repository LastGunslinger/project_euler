prompt = '''

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
'''
from itertools import permutations

from project_euler.utilities import is_prime, list_to_int


def solve():
    logger.debug(prompt)
    number = list(range(1, 10))
    largest = 0
    while len(number) >= 4:
        for pandigital in permutations(number):
            logger.debug(pandigital)
            if is_prime(list_to_int(pandigital)) and list_to_int(pandigital) > largest:
                largest = list_to_int(pandigital)
                # logger.debug(pandigital)
        if largest == 0:
            number = number[:-1]
        else:
            return largest
