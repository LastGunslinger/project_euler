'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''
from ..utilities import factors, is_prime


def solve():
    number = 600851475143
    prime_factors = [x for x in gen_prime_factors(number)]
    print(sorted(prime_factors))
    return max(prime_factors)


def gen_prime_factors(number):
    for x in factors(number):
        if is_prime(x):
            yield x
