'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''
from ..utilities import prime_factors


def solve(logger):
    number = 600851475143
    # prime_factors = [x for x in gen_prime_factors(number)]
    # print(sorted(prime_factors(number)))
    factors = [x[0] for x in prime_factors(number)]
    print(sorted(factors))
    return max(factors)
