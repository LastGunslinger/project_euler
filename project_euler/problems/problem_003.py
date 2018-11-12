prompt = '''

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''
from ..utilities import prime_factors


def solve(logger):
    logger.debug(prompt)
    number = 600851475143
    factors = [x for x in prime_factors(number, exponents=False).keys()]
    print(sorted(factors))
    return max(factors)
