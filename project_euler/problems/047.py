prompt = '''

The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?
'''

from itertools import count
from logging import Logger

from project_euler.utilities import prime_factors


def solve(logger: Logger) -> int:
    logger.debug(prompt)
    start = 646 + 1
    factor_length = 4
    consecutive_target = 4
    result = []

    for number in count(start):
        factors = prime_factors(number, exponents=False)
        if len(factors) == factor_length:
            result.append(number)
            print(result)
        elif not len(factors) == factor_length:
            result = []

        if len(result) == consecutive_target:
            for num in result:
                values = [f'{key}^{val}' for key, val in factors.items()]
                print(f'{num} = {" ".join(values)}')
            return result[0]
